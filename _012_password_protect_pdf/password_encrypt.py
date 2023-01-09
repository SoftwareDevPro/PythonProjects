

from PyPDF2 import PdfWriter, PdfReader
import getpass, sys

pdfwriter = PdfWriter()

pdf = PdfReader(sys.argv[1])

for page_num in range(len(pdf.pages)):
  pdfwriter.add_page(pdf.pages[page_num])

passwrd = getpass.getpass(prompt="Enter a password: ")
pdfwriter.encrypt(passwrd)

with open(sys.argv[2], "wb") as f:
  pdfwriter.write(f)

