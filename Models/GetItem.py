from requests_html import HTMLSession  
from yahoo_fin import stock_info
import yfinance as yf
import pandas as pd
from requests_html import HTMLSession
import pandas as pd

class StockItem:
    def __init__(self) -> None:
        pass

    def getItem(self):
        dow_stocks = stock_info.tickers_dow()
        return dow_stocks
    

class CryptoItem():
    def __init__(self) -> None:
        pass
    
    def getItem(self):
        session = HTMLSession()
        resp = session.get("https://finance.yahoo.com/cryptocurrencies?offset=0&count=100")
        tables = pd.read_html(resp.html.raw_html)
        df = tables[0].copy()
        symbols = df["Symbol"].tolist()
        session.close()
        return symbols
    

class OilItem():
    def __init__(self) -> None:
        pass
    
    def getItem(self):
        session = HTMLSession()
        resp = session.get("https://finance.yahoo.com/sectors/energy/")    
        tables = pd.read_html(resp.html.raw_html)
        df = tables[2].copy()      
        symbols = [item.split(" ")[0] for item in df["Name"].tolist()]
        session.close()
        return symbols

class CurrencyItem():
    def __init__(self) -> None:
        pass
    
    def getItem(self):
        session = HTMLSession()
        resp = session.get("https://finance.yahoo.com/markets/currencies/")
        tables = pd.read_html(resp.html.raw_html)
        df = tables[0].copy()
        symbols = df["Symbol"].tolist()
        session.close()
        return symbols
