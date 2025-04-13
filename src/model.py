import argparse
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.optimizers import Adam
import numpy as np

def train_rf(df):
    X = df[['Return', 'SMA_10', 'RSI']].values[:-1]
    y = df['Close'].values[1:]
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)
    preds = model.predict(X)
    print("RF MSE:", mean_squared_error(y, preds))

def train_lstm(df):
    X = df[['Return', 'SMA_10', 'RSI']].values[:-1]
    y = df['Close'].values[1:]
    X = X.reshape((X.shape[0], 1, X.shape[1]))
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(1, 3)))
    model.add(Dense(1))
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
    model.fit(X, y, epochs=20, verbose=1)
    preds = model.predict(X)
    print("LSTM MSE:", mean_squared_error(y, preds))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', choices=['random_forest', 'lstm'], required=True)
    args = parser.parse_args()

    df = pd.read_csv('data/AAPL_features.csv')
    if args.model == 'random_forest':
        train_rf(df)
    elif args.model == 'lstm':
        train_lstm(df)