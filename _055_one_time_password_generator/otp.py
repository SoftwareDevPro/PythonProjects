

import random

def otp_generate():
    otp = ""
    for idx in range(6):
        otp += str(random.randint(1,9))
    otp += "-"
    for idx in range(6):
        otp += str(random.randint(1,9))
    return otp

if __name__ == "__main__":
    print(otp_generate())

