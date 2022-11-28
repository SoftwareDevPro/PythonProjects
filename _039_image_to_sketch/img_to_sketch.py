

import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-im','--input_image',help='name of the input image')
parser.add_argument('-om','--output_image',help='name of the output image')
args = parser.parse_args()

# read in the image, convert it to grayscale, and invert it.
image = cv2.imread(args.input_image)
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = 255 - grayscale_image

# perform a Gaussian blur on the image, and invert it.
blur = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blur = 255 - blur

sketch = cv2.divide(grayscale_image, inverted_blur, scale=256.0)

# write the output image
cv2.imwrite(args.output_image, sketch)
