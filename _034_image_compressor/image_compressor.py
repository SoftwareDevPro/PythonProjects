

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-if','--input_file',help='name of the input file')
parser.add_argument('-of','--output_file',help='name of the output file')
args = parser.parse_args()

img = Image.open(args.input_file)
img.save(args.output_file, "JPEG", optimize = True, quality = 10)

