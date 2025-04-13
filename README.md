# Stock Price Prediction with ML & Sentiment Analysis

This project forecasts short-term stock price movements using historical time series data combined with sentiment analysis from financial news headlines. It demonstrates both classical machine learning (Random Forest) and deep learning (LSTM) approaches.

---

## Features
- Download historical stock data via `yfinance`
- Scrape or load sentiment from news (sample provided)
- Engineer financial features (RSI, SMA, returns, etc.)
- Train and evaluate Random Forest and LSTM models
- Compare prediction performance
- Optional Streamlit UI for showcasing predictions

---

## Folder Structure
```
stock-prediction-ai/
├── data/                    # Data sources (CSV, raw input)
├── notebooks/              # Jupyter for EDA & prototyping
├── src/                    # Modular Python code
│   ├── data_fetch.py       # Stock data and sentiment loader
│   ├── features.py         # Feature engineering
│   ├── model.py            # Train & test ML/DL models
│   ├── predict.py          # Predict with trained model
│   └── backtest.py         # Simple trading logic
├── streamlit_app.py        # Dashboard UI (optional)
├── requirements.txt
└── README.md
```

## Usage
```bash
pip install -r requirements.txt
python src/data_fetch.py
python src/features.py
python src/model.py --model random_forest
python src/model.py --model lstm
streamlit run streamlit_app.py
```

## License
MIT License