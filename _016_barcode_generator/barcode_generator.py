
import barcode
from barcode.writer import ImageWriter
import sys

output_filename = sys.argv[1]

# Get the number to create the barcode with
barcode_number = input("Enter the code to create barcode: ")

# Get the format of the barcode
barcode_fmt = barcode.get_barcode_class("UPC")

# Generate the barcode and save it
generated_barcode = barcode_fmt(barcode_number, writer=ImageWriter())
generated_barcode.save(output_filename)
