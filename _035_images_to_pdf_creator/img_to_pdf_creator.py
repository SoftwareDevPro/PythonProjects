

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-of','--output_file',help='name of the output pdf')
parser.add_argument('-if', "--input_files", action="store", type=str, nargs="*")
args = parser.parse_args()

def images_to_pdf(files, output):
    images = []

    for file in files:
        image = Image.open(file)
        image = image.convert("RGB")
        images.append(image)

        images[0].save(output, save_all=True, append_images=images[1:])

images_to_pdf(args.input_files, args.output_file)
