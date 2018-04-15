from URLProcessingUtil import URLProcessingUtil
from urllib import parse


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