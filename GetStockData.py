import yfinance as yf

def GetCurrentPrice(tickername):
    stock = yf.Ticker(tickername)
    price = stock.history(period='1min')['Close'].iloc[-1]
    return price

tickername = 'AAPL'
print(GetCurrentPrice(tickername.upper()))