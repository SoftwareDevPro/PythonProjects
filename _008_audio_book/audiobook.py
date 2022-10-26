
import pyttsx3
import sys

book = open(sys.argv[1])
book_text = book.readlines()

engine = pyttsx3.init()

for item in book_text:
   engine.say(item)
   engine.runAndWait()
