import yfinance as yf

class OilMarket:
    def __init__(self,syms):
        self.top_symbols = syms

    def get_current_prices(self):
        oil_data = {}
        for symbol in self.top_symbols:
            data = yf.Ticker(symbol)

            history = data.history(period="1d")
            if history.empty:
                continue 
            
            current_price = history['Close'].iloc[-1] 
            previous_close = history['Close'].iloc[0] if len(history) > 1 else current_price 

            change_percent = ((current_price - previous_close) / previous_close * 100) if previous_close else None
            
            volume = history['Volume'].iloc[-1] if 'Volume' in history.columns else None

            oil_data[symbol] = {
                "buy": current_price * 1.0005, 
                "sell": current_price,          
                "change_percent": change_percent,
                "volume": volume
            }
        return oil_data

    def get_historical_data(self, symbol, period="1mo"):
        data = yf.Ticker(symbol)
        historical_data = data.history(period=period)
        return historical_data

    def get_top_oil_stocks(self):
        return self.top_symbols

if __name__ == "__main__":
    oil_market = OilMarket()

    print(oil_market.get_current_prices())

    print(oil_market.get_historical_data("XOM", period="1mo"))
