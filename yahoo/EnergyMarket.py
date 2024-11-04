import yfinance as yf

class EnergyMarket:
    def __init__(self):
        self.oil_symbol = "CL=F"  # قیمت نفت خام
        self.gas_symbol = "NG=F"  # قیمت گاز طبیعی
        self.symbols = [self.oil_symbol, self.gas_symbol]

    def get_prices(self):
        prices = {}
        for symbol in self.symbols:
            data = yf.Ticker(symbol)
            current_price = data.history(period="1d")['Close'].iloc[-1]
            prices[symbol] = current_price
        return prices

