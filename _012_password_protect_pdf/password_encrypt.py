

from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass, sys

pdfwriter = PdfFileWriter()

pdf = PdfFileReader(sys.argv[1])

for page_num in range(pdf.numPages):
  pdfwriter.addPage(pdf.getPage(page_num))

passwrd = getpass.getpass(prompt="Enter a password: ")
pdfwriter.encrypt(passwrd)

with open(sys.argv[2], "wb") as f:
  pdfwriter.write(f)

