from pydantic import BaseModel
from typing import List
from typing import List, Dict
from datetime import datetime
import yfinance as yf


def get_historical_data(symbols: List[str], start_date: str, end_date: str, interval: str) -> Dict:
    try:
        data = yf.download(symbols, start=start_date, end=end_date, interval=interval)

        if data.empty:
            return {"status": "error", "message": "No data returned for the given symbols and date range."}

        formatted_data = {}

        for column in data.columns:
            feature, symbol = column

            if feature == 'Close' and symbol in symbols:
                if symbol not in formatted_data:
                    formatted_data[symbol] = []

                formatted_data[symbol].extend([
                    {"date": date.isoformat(), "price": row[column]}
                    for date, row in data.iterrows()
                ])

        return {"status": "success", "data": formatted_data}

    except Exception as e:
        return {"status": "error", "message": str(e)}


class HistoricalDataRequest(BaseModel):
    symbols: List[str]
    start_date: str
    end_date: str
    interval: str
