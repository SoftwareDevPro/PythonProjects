

import urllib3, json, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c','--currency',help='currency to check')
args = parser.parse_args()

url = "https://api.exchangerate.host/latest/"
http = urllib3.PoolManager()
response = http.request("GET", url)
data = response.data

data = json.loads(data)
rates = data["rates"]

for curr, rate in rates.items():
    if curr == args.currency:
        print(f"Current Value: {rate}")
        break

