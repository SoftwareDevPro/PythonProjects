

import gofile as go
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f','--file',help='file to store')
args = parser.parse_args()

def store_file(f):
    server = go.getServer()
    print(server)
    url = go.uploadFile(f)
    print(f"download link:{url['downloadPage']}")

store_file(args.file)
