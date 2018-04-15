import argparse
from FrequencyTable import FrequencyTable as ft

def train(c):
	print("######################")
	print("Running Training...")
	print("######################")
	samplePhishingData = ["http:\\www.website.com", "https:\\www.ucd.gov", "https:\\www.jesus.gov?give.me/bank"]
	for url in samplePhishingData:
		c.run_training(url, True)

	sampleSafeData = ["https:\\www.youtube.com", "http:\\www.dcu.ie"]
	for url in sampleSafeData:
		c.run_training(url, False)

	print("######################")
	print("Training Done.")
	print("######################")

def classify(c, url):
	c.run_tests(url)

def main(args):
    c = ft()

    print(args)

    if args.train:
    	train(c)

    if args.classify:
    	classify(c, args.classify)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Classify URLs")
	parser.add_argument("-t", "--train", dest='train', action='store_true', help='Run Training on Data')
	parser.add_argument("-c", dest='classify', action='store', help='Classify Url')
	parser.add_argument("-f", "--file",
                        dest="filename",
                        type=lambda x: is_valid_file(parser, x),
                        help="write report to FILE",
                        metavar="FILE")

	args = parser.parse_args()

	main(args)