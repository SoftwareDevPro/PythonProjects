
from captcha.image import ImageCaptcha
import argparse

# Parse the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-t','--text',help='text to use in captcha')
parser.add_argument('-o','--output_img',help='the output image filename')
args = parser.parse_args()

# Setup the CAPTCHA image
image = ImageCaptcha(width=400, height=200)

# Grab the text for the captcha and generate the image
captcha_text = args.text
data = image.generate(captcha_text)

# Write the image
image.write(captcha_text, args.output_img)
