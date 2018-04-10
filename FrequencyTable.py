from Record import Record
from URLTests import URLTests


class FrequencyTable:

    frequency_table = {}

    def __init__(self):
        self.total_number_of_entries = 0
        self.total_number_of_positives = 0
        self.total_number_of_negatives = 0
        self.positive_prior = 0
        self.negative_prior = 0
        self.test_methods = []
        for method in dir(URLTests):
            if method.startswith("test"):
                self.frequency_table[method] = Record()
                self.test_methods.append(method)

    def run_training(self, url, phishing):
        self.total_number_of_entries += 1
        if phishing:
            self.positive_prior += 1
        else:
            self.negative_prior += 1
        for method in self.test_methods:
            if getattr(URLTests, method)(url):
                self.frequency_table.get(method).increment_num_of_occurrences()
                if phishing:
                    self.frequency_table.get(method).increment_num_of_positives()
                    self.total_number_of_positives += 1
                else:
                    self.frequency_table.get(method).increment_num_of_negatives()
                    self.total_number_of_negatives += 1

    def print_library(self):
        print("key \t occurrences \t positives \t negatives")
        for key in self.frequency_table.keys():
            record = self.frequency_table.get(key)
            print(key + "\t" + str(record.get_num_of_occurrences()) + "\t\t\t\t" + str(record.get_num_of_positives())
                  + "\t\t\t" + str(record.get_num_of_negatives()))

    def get_positive_prior(self):
        return self.positive_prior / self.total_number_of_entries

    def get_negative_prior(self):
        return self.negative_prior / self.total_number_of_entries

    def get_check_positive_likelihood(self, key):
        return (self.frequency_table.get(key).get_num_of_positives() + 1) \
            / (self.total_number_of_positives + self.frequency_table.keys().__len__())

    def get_check_negative_likelihood(self, key):
        return (self.frequency_table.get(key).get_num_of_negatives() + 1) \
            / (self.total_number_of_negatives + self.frequency_table.keys().__len__())

    def get_positive_prob(self):
        self.get_positive_prior()

    def run_tests(self, url):
        passed_tests = []
        for method in self.test_methods:
            if getattr(URLTests, method)(url):
                passed_tests.append(method)

        prob = self.get_positive_prior()
        for passedtest in passed_tests:
            prob = prob * self.get_check_positive_likelihood(passedtest)
        print("prob = " + str(prob))