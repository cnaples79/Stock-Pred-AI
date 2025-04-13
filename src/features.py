import pandas as pd

def compute_features(input_path, output_path):
    df = pd.read_csv(input_path, index_col='Date', parse_dates=True)
    df['Return'] = df['Close'].pct_change()
    df['SMA_10'] = df['Close'].rolling(10).mean()
    df['RSI'] = compute_rsi(df['Close'])
    df = df.dropna()
    df.to_csv(output_path)
    print(f"Saved features to {output_path}")

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

if __name__ == '__main__':
    compute_features('data/AAPL_raw.csv', 'data/AAPL_features.csv')