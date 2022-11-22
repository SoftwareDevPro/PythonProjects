

import PyPDF2
import pyttsx3
import argparse

# Parse the program argument
parser = argparse.ArgumentParser()
parser.add_argument('-if','--input_file',help='document to read')
args = parser.parse_args()

# Open the file for reading, and create a PDF object from it
path = open(args.input_file, "rb")
reader = PyPDF2.PdfFileReader(path)

# Initialize the speech synthesis engine
speak = pyttsx3.init()

# Loop through the whole document, extracting the text, and read it
for page in range(reader.numPages):
    text = reader.getPage(page).extractText()
    speak.say(text)
    speak.runAndWait()

speak.stop()
