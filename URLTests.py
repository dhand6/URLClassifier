from Utils import tokenize_url
from urllib import parse


class URLTests:

    #Checks to see if the URL starts with 'https'.
    @staticmethod
    def test_one(url):
        b = False
        if not url.startswith(("https://", "http://")):
            b = True
        print("Test One Results: " + str(b))
        return b


    @staticmethod
    def test_two(url):
        extensions = [".gov", ".exe", ".ru"]
        b = False
        if any(e in url for e in extensions):
            b = True
        print("Test Two Results: " + str(b))
        return b

    @staticmethod
    def test_three(url):
        sen_words = ['confirm', 'account', 'login', 'signin', 'banking', 'bank']
        count = 0
        token_words = tokenize_url(url)
        b = False
        for e in token_words:
            if e in sen_words:
                b = True
        print("Test Three Results: " + str(b))
        return b

    # @staticmethod
    # def test_four(url):
    #     print(url)
    #     #URLProcessingUtil.getURLRedirects(url)
    #     print(URLProcessingUtil.getURLHostName(url))
    #     print(URLProcessingUtil.getURLDomainName(url))
    #     URLProcessingUtil.getURLIPAddress(url)
    #     res = URLProcessingUtil.getWhoIs(url)
    #     URLProcessingUtil.getResAddress(res)
    #     URLProcessingUtil.getResAddressCountry(res)
    #     URLProcessingUtil.getResCountry(res)
    #     URLProcessingUtil.getResRange(res)
    #
    #
    #     return False
    #
    # @staticmethod
    # def test_http_is_secure(url):
    #     scheme = '{uri.scheme}'.format(uri=parse.urlparse(url))
    #     if scheme.__eq__("https"):
    #         return True
    #     return False
    #
    # @staticmethod
    # def test_http_not_secure(url):
    #     scheme = '{uri.scheme}'.format(uri=parse.urlparse(url))
    #     if scheme.__eq__("http"):
    #         return True
    #     return False
    #
    # @staticmethod
    # def test_http_not_secure(url):
    #     scheme = '{uri.scheme}'.format(uri=parse.urlparse(url))
    #     if scheme.__eq__("http"):
    #         return True
    #     return False