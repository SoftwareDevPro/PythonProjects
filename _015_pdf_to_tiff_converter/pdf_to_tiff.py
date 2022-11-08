
import aspose.words as aw
import os.path
import sys

pdf_file = sys.argv[1]
pdf_dir = os.path.dirname(pdf_file)
pdf_basename = os.path.splitext(pdf_file)[0]

# Load up the PDF document
doc = aw.Document(pdf_file)

# Convert the document to TIFF format
doc.save(pdf_dir + os.path.sep + pdf_basename + ".tiff")


