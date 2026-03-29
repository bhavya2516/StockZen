import yfinance as yf

def get_stock_data(ticker):
    return yf.Ticker(ticker).history(period="1y")