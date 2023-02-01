

import pikepdf
from tqdm import tqdm
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('-wl','--wordlist',help='file with word list')
parser.add_argument('-if','--input_file',help='file to attempt to get password from')
args = parser.parse_args()


passwords = [ line.strip() for line in open("rockyou.txt", encoding="latin-1") ]

for password in tqdm(passwords, "Decrypting PDF"):
    try:
        with pikepdf.open("encrypted_pdf_document.pdf", password=password) as pdf:
            print("\n[+] Password found: ", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # incorrect password, simply go on to the next one
        continue

