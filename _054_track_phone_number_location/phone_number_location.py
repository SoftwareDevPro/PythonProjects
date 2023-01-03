

import phonenumbers
from phonenumbers import geocoder
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('-n','--number',help='the phone number including country code')
parser.add_argument('-l','--lang',help='the language to output', default='en')
args = parser.parse_args()

phone_number = phonenumbers.parse(args.number)
# "+13607867018"
print(phonenumbers.geocoder.description_for_number(phone_number,args.lang))
