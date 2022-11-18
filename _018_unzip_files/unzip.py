

from zipfile import ZipFile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f','--file',help='file to unzip')
args = parser.parse_args()

# Extract all the files from the Zip file
with ZipFile(args.file, "r") as zip_object:
  zip_object.extractall()

# Print a list of files that are archived in the ZIP file
print(zip_object.namelist())

