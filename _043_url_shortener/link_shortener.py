
import pyshorteners
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u','--url',help='the url to shorten')
args = parser.parse_args()

shortener = pyshorteners.Shortener()
# shortener.available_shorteners gives list of available shorteners
shortened_url = shortener.chilpit.short(args.url)

print("Shortened URL is: ", shortened_url)
