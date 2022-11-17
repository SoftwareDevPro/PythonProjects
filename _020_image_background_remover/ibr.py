

from rembg import remove
from PIL import Image
import sys
import os.path

input_image = sys.argv[1]
input_directory = os.path.dirname(input_image)
input_basename = os.path.basename(input_image)
input_filename = os.path.splitext(input_basename)[0]

output_image = f"{input_directory}{os.path.sep}{input_filename}.png"

img = Image.open(input_image)
output = remove(img)
output.save(output_image)
