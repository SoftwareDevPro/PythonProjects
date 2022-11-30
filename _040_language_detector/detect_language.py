

from langdetect import detect
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t','--text',help='text to detect language from')
args = parser.parse_args()

print(detect(args.text))

