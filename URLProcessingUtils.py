import requests
import socket
from ipwhois import IPWhois
from urllib import parse
import pycountry
import re

def tokenize_url(url):
    if url == '':
        return "url cannot be tokenized as it's empty"
    else:
        tokens = re.split('\W+', url)
        return tokens

def getURLRedirects(url):
    try:
        r = requests.get(url)
        return r.history
    except (requests.exceptions.SSLError, requests.exceptions.ConnectionError):
        print(str(url) + " ::is no longer active")

def getURLHostName(url):
    parsed_uri = parseURL(url)
    if parsed_uri != None:
        return '{uri.netloc}'.format(uri=parsed_uri)
    else:
        return None

def getURLDomainName(url):
    parsed_uri = parseURL(url)
    if parsed_uri != None:
        return '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    else:
        return None

def getURLIPAddress(url):
    parsed_uri = parseURL(url)
    if parsed_uri != None:
        try:
            return socket.gethostbyname('{uri.netloc}'.format(uri=parsed_uri))
        except socket.gaierror:
            print(str(url) + ":: cannot get host name")
            return None
    else:
        return None

def getWhoIs(url):
    ip = getURLIPAddress(url)
    if ip != None:
        obj = IPWhois(ip)
        return obj.lookup_whois()
    else:
        return None

def getResAddress(res):
    if res != None:
        return res["nets"][0]['address']
    else:
        return None

def getResAddressCountry(res):
    address = getResAddress(res)
    if address != None:
        country = address.split("\n")[-1:]
        for c in pycountry.countries:
            if c.name.lower() == country[0].lower():
                return country[0].lower()
    else:
        return None

def getResCountry(res):
    if res != None:
        return res["nets"][0]['country']
    else:
        return None

def getResRange(res):
    if res != None:
        return res["nets"][0]['range']
    else:
        return None

def parseURL(url):
    try:
        return parse.urlparse(url)
    except socket.gaierror:
        print(str(url) + ":: cannot be parsed")