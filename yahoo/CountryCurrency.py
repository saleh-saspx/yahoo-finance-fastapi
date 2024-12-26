import yfinance as yf

class CountryCurrency:
    def __init__(self,syms):
            self.top_symbols = syms


    def get_current_prices(self):
        prices = {}
        for symbol in self.top_symbols:
            try:
                data = yf.Ticker(symbol)
                history = data.history(period="5d", interval="1d")
                if not history.empty:
                    current_price = history['Close'].iloc[-1]
                    previous_close = history['Close'].iloc[0]
                    change_percent = ((current_price - previous_close) / previous_close) * 100 if previous_close else None
                    
                    prices[symbol] = {
                        "buy": current_price * 1.0005,  
                        "sell": current_price,          
                        "change_percent": change_percent,
                        'info': data.info              
                    }
                else:
                    prices[symbol] = {
                        "buy": None,
                        "sell": None,
                        "change_percent": None,
                        'info': None
                    }
            except Exception as e:
                prices[symbol] = {
                    "buy": None,
                    "sell": None,
                    "change_percent": None,
                    'info': None
                }

        return prices

    def get_historical_data(self, symbol, period="1mo"):
        data = yf.Ticker(symbol)
        historical_data = data.history(period=period)
        return historical_data

    def get_forex_symbols(self):
        return self.top_symbols
