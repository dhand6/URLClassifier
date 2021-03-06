from URLProcessingUtils import tokenize_url
from urllib import parse
from urllib.request import urlopen
import ssl
import urllib.request
import re
from URLProcessingUtils import getURLIPAddress
from DBConnector import DBConnector

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

class URLTests:

    #Checks to see if the URL starts with 'https'.
    @staticmethod
    def test_one(url):
        b = False
        if not url.startswith(("https://", "http://")):
            b = True
        return b


    @staticmethod
    def test_two(url):
        extensions = [".exe", ".ru", ".com.", ".org.", ".net.", ".int.", ".edu.", ".gov.", ".mil."]
        b = False
        if any(e in url for e in extensions):
            b = True
        return b

    @staticmethod
    def test_three(url):
        sen_words = ['confirm', 'account', 'login', 'signin', 'banking', 'bank', '000webhostapp']
        count = 0
        token_words = tokenize_url(url)
        b = False
        for e in token_words:
            if e in sen_words:
                b = True
        return b

    @staticmethod
    def test_four(url):
        b = False
        try:
            source = str(urlopen(url, context=scontext, timeout=1).read())
            c = source.count('<iframe')
            if c > 0:
                b = True
        except Exception as e:
            print("Error " + str(e) + " in downloading page " + url)
            b = True
        return b

        #print("Test Three Results: " + str(b))
        return b

    @staticmethod
    def test_url_contains_ip_address(url):
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', url)
        if ip != None:
            return True
        return False

    @staticmethod
    def test_ip_blacklisted(url):
        ip = getURLIPAddress(url)
        if DBConnector().is_ip_blacklisted(ip):
            return True
        return False

    # @staticmethod
    # def test_four(url):
    #     b = False
    #     try:
    #         source = str(op.open(url))
    #         c = source.count('<iframe')
    #         if c > 0:
    #             b = True
    #     except Exception as e:
    #         print("Error " + str(e) + " in downloading page " + "url")
    #     return b
    
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