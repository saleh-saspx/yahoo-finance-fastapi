import yfinance as yf

class CryptocurrencyMarket:
    def __init__(self,syms):
        self.top_symbols = syms
    
    def get_current_prices(self):
        current_prices = {}
        for symbol in self.top_symbols:
            data = yf.Ticker(symbol)
            current_price = data.info['last_price'] if 'last_price' in data.info else data.history(period="1d")['Close'].iloc[-1]
            current_prices[symbol] = {
                "sell" : current_price,
                'buy' : current_price  * 1.0005,
                'info' : data.info   
            }
        return current_prices

    def get_historical_data(self, symbol, period="1mo"):
        data = yf.Ticker(symbol)
        historical_data = data.history(period=period)
        return historical_data

    def get_top_cryptocurrencies(self):
        return self.top_symbols


