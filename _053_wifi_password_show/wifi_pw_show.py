
import subprocess

data = subprocess.check_output(["netsh",
                                "wlan",
                                "show",
                                "profiles"]).decode("UTF-8").split("\n")

# Grab just the profile lines
profiles = [  idx.split(":")[1][1:-1] for idx in data if "All User Profile" in idx]

for profile in profiles:
    results = subprocess.check_output(["netsh", 
                                       "wlan", 
                                       "show",
                                       "profile", profile,
                                       "key=clear"]).decode("UTF-8").split("\n")

    # Grab the password (Key content)
    results = [ b.split(":")[1][1:-1] for b in results if "Key Content" in b]

    try:
        print("{:40}|  {:<}".format(profile, results[0]))
    except IndexError:
        print("{:40}|  {:<}".format(profile, ""))
