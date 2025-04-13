import yfinance as yf
import pandas as pd

TICKER = 'AAPL'
START = '2020-01-01'
END = '2023-01-01'

def fetch_stock_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df.to_csv(f'data/{ticker}_raw.csv')
    print(f"Saved data to data/{ticker}_raw.csv")

if __name__ == '__main__':
    fetch_stock_data(TICKER, START, END)