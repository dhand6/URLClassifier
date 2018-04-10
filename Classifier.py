from FrequencyTable import FrequencyTable
import csv

c = FrequencyTable()

#with open('verified_online.csv') as csvfile:
#    readCSV = csv.reader(csvfile, delimiter=',')
#    for row in readCSV:
#        print(row[1])

samplePhishingData = ["http:\\website.com", "https:\\ucd.gov", "https:\\jesus.gov"]
for url in samplePhishingData:
    c.run_training(url, True)

sampleSafeData = ["https:\\youtube.com", "http:\\dcu.ie"]
for url in sampleSafeData:
    c.run_training(url, False)
c.print_library()

c.run_tests("https\\fishing.gov")



