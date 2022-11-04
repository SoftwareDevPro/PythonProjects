
import pyqrcode
import sys

# Pull the string to encode from the command line
string_to_encode = sys.argv[1]

# Generate the QR code
qrcode = pyqrcode.create(string_to_encode)

# Grab the base filename for the output images
base_filename = sys.argv[2]

# Output a SVG and PNG
qrcode.svg(f"{base_filename}.svg", scale=10)
qrcode.png(f"{base_filename}.png", scale=8)


