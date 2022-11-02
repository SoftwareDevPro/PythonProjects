

from PyPDF2 import PdfFileMerger
import os, sys

merger = PdfFileMerger()

for item in os.listdir():
  if item.endswith(".pdf") and item != sys.argv[1]:
    merger.append(item)

merger.write(sys.argv[1])

merger.close()



