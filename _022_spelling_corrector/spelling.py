

from textblob import TextBlob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-w','--words',help='words to check')
args = parser.parse_args()

words_to_check = args.words
words = list(words_to_check.split())
corrected_words = []

for word in words:
    corrected_words.append(TextBlob(word))

print(f"Words: {' '.join(words)}")
cstr = [ str(word.correct()) for word in corrected_words ]
print(f"Corrected Words: {' '.join(cstr)}")

