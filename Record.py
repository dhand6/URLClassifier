class Record:

    num_of_occurrences = 0
    num_of_positives = 0
    num_of_negatives = 0

    def get_num_of_occurrences(self):
        return self.num_of_occurrences

    def get_num_of_positives(self):
        return self.num_of_positives

    def get_num_of_negatives(self):
        return self.num_of_negatives

    def increment_num_of_occurrences(self):
        self.num_of_occurrences += 1

    def increment_num_of_positives(self):
        self.num_of_positives += 1

    def increment_num_of_negatives(self):
        self.num_of_negatives += 1
