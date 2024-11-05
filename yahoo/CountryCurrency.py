import yfinance as yf

class CountryCurrency:
    def __init__(self,syms):
            self.top_symbols = syms

    def get_current_prices(self):
        prices = {}
        for symbol in self.top_symbols:
            data = yf.Ticker(symbol)
            current_price = data.history(period="1d")['Close'].iloc[-1]
            previous_close = data.history(period="1d")['Close'].iloc[0]  
            change_percent = ((current_price - previous_close) / previous_close) * 100 if previous_close else None
            prices[symbol] = {
                "buy": current_price * 1.0005,      
                "sell": current_price,               
                "change_percent": change_percent, 
                'info' : data.info   
            }
        return prices

    def get_historical_data(self, symbol, period="1mo"):
        data = yf.Ticker(symbol)
        historical_data = data.history(period=period)
        return historical_data

    def get_forex_symbols(self):
        return self.top_symbols

if __name__ == "__main__":
    forex_market = CountryCurrency()
    current_prices = forex_market.get_current_prices()
    for symbol, details in current_prices.items():
        print(f"{symbol}: {details}")

  