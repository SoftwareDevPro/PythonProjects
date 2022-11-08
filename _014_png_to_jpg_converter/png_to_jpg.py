
from PIL import Image
import os.path
import sys

png_file = sys.argv[1]
png_dir = os.path.dirname(png_file)
png_basename = os.path.splitext(png_file)[0]

# Open the image and convert to RGB
img = Image.open(png_file)
rgb_img = img.convert("RGB")

# Output the image in JPEG format
rgb_img.save(png_dir + os.path.sep + png_basename + ".jpg")

