import yfinance as yf
import numpy as np

def get_stock_statistics(ticker, period='1y'):
    # Download stock data
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    
    # Calculate daily returns
    data['Returns'] = data['Close'].pct_change()
    
    # Drop NaN values
    data = data.dropna()
    
    # Calculate expected value (mean return)
    expected_value = np.mean(data['Returns'])
    
    # Calculate standard deviation (volatility)
    std_dev = np.std(data['Returns'])
    
    return expected_value, std_dev

if __name__ == "__main__":
    ticker = input("Enter stock ticker symbol (e.g., AAPL, TSLA): ").upper()
    expected_value, std_dev = get_stock_statistics(ticker)
    
    print(f"Stock: {ticker}")
    print(f"Expected Daily Return: {expected_value:.6f} ({(expected_value*100):.4f}%)")
    print(f"Standard Deviation of Daily Returns: {std_dev:.6f} ({(std_dev*100):.4f}%)")