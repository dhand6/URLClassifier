import pymysql

class DBConnector(object):

    __dbConection = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnector, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.__dbinit()

    def __connectToDB__(self):
        try:
            self.__dbConection = pymysql.connect("localhost", "user", "password", "url_classifier")
            # prepare a cursor object using cursor() method
            return self.__dbConection.cursor()
        except pymysql.err.InternalError:
            if self.__dbConection != None:
                self.__dbConection.close()

    def __closeDBConection(self):
        if self.__dbConection != None:
            self.__dbConection.close()

    def __runQuery(self, query, args):
        returnValue = None
        try:
            cursor = self.__connectToDB__()
            cursor.execute(query, args)
            returnValue = cursor.fetchone()
            self.__dbConection.commit()
        except Exception as e:
            print(e)
        finally:
            self.__closeDBConection()
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
                cursor.execute("CREATE TABLE url_info (Url TEXT, Hostname VARCHAR(255), IPAddress VARCHAR(255), Region VARCHAR(255), IPRange VARCHAR(255) );")
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

    def increment_num_of_occurrences(self, test_name):
        self.__runQuery("UPDATE records SET occurrences=occurrences+1 WHERE testName = %s", (str(test_name),))

    def increment_num_of_positives(self, test_name):
        self.__runQuery("UPDATE records SET positives=positives+1 WHERE testName = %s", (str(test_name),))

    def increment_num_of_negatives(self, test_name):
        self.__runQuery("UPDATE records SET negatives=negatives+1 WHERE testName = %s", (str(test_name),))

    def create_record(self, test_name):
        self.__runQuery("INSERT INTO records(testName) VALUES(%s);", (str(test_name),))

    def get_number_of_tests(self):
        return self.__runQuery("SELECT COUNT(testName) FROM records;", ())[0]






