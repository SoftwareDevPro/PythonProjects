

import yfinance as yf
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('-s','--stock',help='stock to get market price')
args = parser.parse_args()

if __name__ == '__main__':
    stock = args.stock
    share = yf.Ticker(stock).info
    market_price = share['regularMarketPrice']
    
    print(market_price)
