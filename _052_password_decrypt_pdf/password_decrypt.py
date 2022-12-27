
from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-if','--input_file',help='the input encrypted PDF file')
parser.add_argument('-pw','--password',help='the password to the PDF file')
args = parser.parse_args()

writer = PdfFileWriter()

input_file = args.input_file
reader = PdfFileReader(input_file)

if reader.isEncrypted:
    reader.decrypt(args.password)

    for page in range(reader.numPages):
        writer.addPage(reader.getPage(page))

    with open(input_file,"wb") as output_file:
        writer.write(output_file)
        output_file.close()

    print("File decrypted successfully")
else:
    print("File is not encrypted")

