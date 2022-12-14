

from pyzbar.pyzbar import decode
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-if','--input_file',help='name of input file image of QR code')
args = parser.parse_args()

decoded_qr_code = decode(Image.open(args.input_file))
print(decoded_qr_code[0].data.decode("ASCII"))
