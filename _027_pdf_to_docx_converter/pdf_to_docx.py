

from pdf2docx import Converter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-if','--input_file',help='file to convert')
parser.add_argument('-of','--output_file',help='name of output file')
args = parser.parse_args()

pdf_file = args.input_file
docx_file = args.output_file

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()


