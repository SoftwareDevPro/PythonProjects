
import pyqrcode
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t','--text',help='text to encode in a QR code')
parser.add_argument('-of','--output_file',help='name of output file w/o extension')

args = parser.parse_args()

# Pull the string to encode from the command line
string_to_encode = args.text

# Generate the QR code
qrcode = pyqrcode.create(string_to_encode)

# Grab the base filename for the output images
base_filename = args.output_file

# Output a SVG and PNG
qrcode.svg(f"{base_filename}.svg", scale=10)
qrcode.png(f"{base_filename}.png", scale=8)


