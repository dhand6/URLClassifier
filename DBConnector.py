import pymysql


class DBConnector(object):

    __dbConnection = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnector, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.__dbinit()

    def __connectToDB__(self):
        try:
            self.__dbConnection = pymysql.connect("localhost", "user", "password", "url_classifier")
            # prepare a cursor object using cursor() method
            return self.__dbConnection.cursor()
        except pymysql.err.InternalError:
            if self.__dbConnection != None:
                self.__dbConnection.close()

    def __closeDBConnection(self):
        if self.__dbConnection != None:
            self.__dbConnection.close()

    def __runQuery(self, query, args):
        returnValue = None
        try:
            cursor = self.__connectToDB__()
            cursor.execute(query, args)
            returnValue = cursor.fetchone()
            self.__dbConnection.commit()
        except Exception as e:
            print(e)
        finally:
            self.__closeDBConnection()
            return returnValue


    def __dbinit(self):
        dbCon = None
        dbExists = False
        try:
            dbCon = pymysql.connect("localhost", "user", "password")
            cursor = dbCon.cursor()
            cursor.execute("SHOW DATABASES;")
            for db in cursor.fetchall():
                if db[0] == "url_classifier":
                    dbExists = True
            if not dbExists:
                cursor.execute("CREATE DATABASE url_classifier;")
                cursor.execute("USE url_classifier;")
                cursor.execute("CREATE TABLE url_info (ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, Url TEXT, Hostname VARCHAR(255), IPAddress VARCHAR(255), Region VARCHAR(255), IPRange VARCHAR(255), Phishing BIT);")
                cursor.execute("CREATE TABLE country_info(Country varchar(255), TimesOccured int);")
                cursor.execute("CREATE TABLE records(testName varchar(255) UNIQUE, occurrences int DEFAULT 0, positives int DEFAULT 0, negatives int DEFAULT 0);")
        except pymysql.err.InternalError as e:
            print(e)
        finally:
            if dbCon != None:
                dbCon.close()

    def get_num_of_occurrences(self, test_name):
        return self.__runQuery("SELECT occurrences from records WHERE testName = %s", (str(test_name),))[0]

    def get_num_of_positives(self, test_name):
        return self.__runQuery("SELECT positives from records WHERE testName = %s", (str(test_name),))[0]

    def get_num_of_negatives(self, test_name):
        return self.__runQuery("SELECT negatives from records WHERE testName = %s", (str(test_name),))[0]

    def get_total_num_of_positives(self):
        return self.__runQuery("SELECT SUM(positives) from records", ())[0]

    def get_total_num_of_negatives(self):
        return self.__runQuery("SELECT SUM(negatives) from records", ())[0]

    def increment_num_of_occurrences(self, test_name):
        self.__runQuery("UPDATE records SET occurrences=occurrences+1 WHERE testName = %s", (str(test_name),))

    def increment_num_of_positives(self, test_name):
        self.__runQuery("UPDATE records SET positives=positives+1 WHERE testName = %s", (str(test_name),))

    def increment_num_of_negatives(self, test_name):
        self.__runQuery("UPDATE records SET negatives=negatives+1 WHERE testName = %s", (str(test_name),))

    def create_record(self, test_name):
        self.__runQuery("INSERT INTO records(testName) VALUES(%s);", (str(test_name),))

    def create_url_info(self, url, phishing, host_name, ip_address, res_range, res_country):
        self.__runQuery("INSERT INTO url_info(URL,Phishing,Hostname,IPAddress,IPRange,Region) VALUES(%s,%s,%s,%s,%s,%s);", (url, phishing,host_name, ip_address, res_range, res_country))

    def get_number_of_tests(self):
        return self.__runQuery("SELECT COUNT(testName) FROM records;", ())[0]

    def get_positive_prior(self):
        return self.__runQuery("SELECT COUNT(Phishing) FROM url_info WHERE Phishing = TRUE;", ())[0]

    def get_negative_prior(self):
        return self.__runQuery("SELECT COUNT(Phishing) FROM url_info WHERE Phishing = FALSE;", ())[0]

    def get_total_number_of_entries(self):
        return self.__runQuery("SELECT COUNT(ID) FROM url_info;", ())[0]

    def is_ip_blacklisted(self, ip):
        return self.__runQuery("SELECT COUNT(IPAddress) FROM url_info WHERE IPAddress = %s AND Phishing = TRUE;", (ip,))[0]






