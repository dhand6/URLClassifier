from URLTests import URLTests
from DBConnector import DBConnector
from decimal import Decimal


class FrequencyTable:

    def __init__(self):
        self.test_methods = []
        for method in dir(URLTests):
            if method.startswith("test"):
                DBConnector().create_record(method)
                self.test_methods.append(method)

    def run_training(self, url, phishing):
        DBConnector().create_url_info(url, phishing)
        for method in self.test_methods:
            if getattr(URLTests, method)(url):
                DBConnector().increment_num_of_occurrences(method)
                if phishing:
                    DBConnector().increment_num_of_positives(method)
                else:
                    DBConnector().increment_num_of_negatives(method)

    def get_positive_prior(self):
        return DBConnector().get_positive_prior() / DBConnector().get_total_number_of_entries()

    def get_negative_prior(self):
        return DBConnector().get_negative_prior() / DBConnector().get_total_number_of_entries()

    def get_check_positive_likelihood(self, key):
        return (DBConnector().get_num_of_positives(key) + 1) \
            / (DBConnector().get_total_num_of_positives() + DBConnector().get_number_of_tests())

    def get_check_negative_likelihood(self, key):
        return (DBConnector().get_num_of_negatives(key) + 1) \
            / (DBConnector().get_total_num_of_negatives() + DBConnector().get_number_of_tests())

    def run_tests(self, url):
        passed_tests = []
        for method in self.test_methods:
            if getattr(URLTests, method)(url):
                passed_tests.append(method)

        prob = self.get_positive_prior()
        for passedtest in passed_tests:
            prob = Decimal(prob) * self.get_check_positive_likelihood(passedtest)
        print("prob of phishing = " + str(prob))

        prob = self.get_negative_prior()
        for passedtest in passed_tests:
            prob = Decimal(prob) * self.get_check_negative_likelihood(passedtest)
        print("prob not phishing = " + str(prob))
