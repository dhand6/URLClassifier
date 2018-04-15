from FrequencyTable import FrequencyTable
from DBConnector import DBConnector
from URLTests import URLTests
import csv

c = FrequencyTable()

# with open('verified_online.csv') as csvfile:
#    readCSV = csv.reader(csvfile, delimiter=',')
#    for row in readCSV:
#        print(row[1])
#        URLTests.test_four(row[1])

samplePhishingData = ["http:\\www.website.com", "https:\\www.ucd.gov", "https:\\www.jesus.gov"]
for url in samplePhishingData:
   c.run_training(url, True)

sampleSafeData = ["https:\\www.youtube.com", "http:\\www.dcu.ie"]
for url in sampleSafeData:
   c.run_training(url, False)
#c.print_library()

c.run_tests("https\\fishing.gov")
#URLTests.test_four("http://fb-shieldprotect500000.000webhostapp.com/Payment-update-0.html?fb_source=bookmark_apps&amp")
#URLTests.test_four("http://links.spotify.com/u/click?_t=1090098043a54e4ca3e92096868a66e3&_m=4142fc74c02348d8bb84175eb419d9e6&_e=ptwtiu5bPDWnSykUwJ6SRQilerqX565mA9-M2vXe7_NLfqv0OLfXdVWWIcZaX58wy0av3viWVfmC7_gSiPU8N83_WDoET5HMR6g6rLnI_o0xhU4DHw9GP66I0vF-1rt1SQrZWaMM8G7d06aLu7lGQ9uleAqrorbVOqcJyQat_q-HXuHkgWXmkvgSguI1yo0M4OEh4xwxIbiujGX5MYZV1WMQ5AkQox1TOWUhCNwo2eILZYVEIUkKldzz4SAnKxexQqXN6gr4giRpMA1JeeEMjZsVnQ-KKaaHNFQCJvx8Kq5AAFe1fS1nB1ijyWFY3Dp7UvcWBImynbWVrXwpZ-PYX64tvVqD6IGYdg5CwiO8wJlBbgNKU-dW_P3ms5pKuHWFkLqma91HC1USNr1sv9tPV8EmNppVIzTC8U6CZx6fMNrF8exSNeqbFnN2NtGoee1LrvuNVH-ZoRRsf5PrMlW4GPWQ43M5sU2RUv_lxanD3JGF06_GX9mFcHKlL_xsG5Rsm8U4SSJBbZnFSio7J6XQpQ1PGRKY9OZrdjj58ONGV3w%3D")
#URLTests.test_four("https://hostmacau.com/~!@%23$%25^&*()_+~!@%23$%25^&*()_+/strdropbox-final/")
#print(DBConnector())

#DBConnector().__connectToDB__()

