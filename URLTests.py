class URLTests:

    @staticmethod
    def test_one(url):
        if url.startswith("https"):
            return True
        return False

    @staticmethod
    def test_two(url):
        if url.endswith(".com"):
            return True
        return False

    @staticmethod
    def test_three(url):
        if url.endswith(".gov"):
            return True
        return False