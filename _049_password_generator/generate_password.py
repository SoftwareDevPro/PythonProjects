
import random
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l','--length',help='the length of password to generate')
args = parser.parse_args()

def generate_password():
    pw_characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for x in range(int(args.length)):
        password = password + random.choice(pw_characters)
    
    return password

print(generate_password())