

from forex_python.converter import CurrencyRates
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a','--amount',help='amount to convert')
parser.add_argument('-f','--from_curr',help='the currency to convert from')
parser.add_argument('-t','--to_curr',help='the currency to convert to')
args = parser.parse_args()

rates = CurrencyRates()

amount = float(args.amount)
from_curr = args.from_curr.upper()
to_curr = args.to_curr.upper()

result = rates.convert(from_curr, to_curr, amount)
print(f"{amount} {from_curr} = {round(result,2)} {to_curr}")
