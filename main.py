from requests_html import HTMLSession  
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis
from pydantic import BaseModel
from typing import List
from response import clean_data
from yahoo.CryptocurrencyMarket import CryptocurrencyMarket
from yahoo.StockMarket import StockMarket
from yahoo.CountryCurrency import CountryCurrency
from yahoo.OilMarket import OilMarket
from Models.RequestData import DataModel
from Models.GetItem import StockItem,CryptoItem,OilItem,CurrencyItem
from yahoo.CryptoCurrencyHistoryCall import HistoricalDataRequest , get_historical_data

class Item(BaseModel):
    buy: float
    sell: float

class ResponseModel(BaseModel):
    items: List[Item]

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost:6371")
    try:
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
        yield
    finally:
        await redis.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"status": "up !"}

@app.post("/yahoo/crypto", response_model=ResponseModel)
@cache(expire=60 * 12)
async def get_crypto_price(DataModel:DataModel):
    try:
        crypto_market = CryptocurrencyMarket(DataModel.items)
        cleaned_data = clean_data({
            "items": crypto_market.get_current_prices()
        })  
        return JSONResponse(content=cleaned_data) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/yahoo/stock", response_model=ResponseModel)
@cache(expire=60 * 12)
async def get_stocks_price(DataModel:DataModel):
    try:
        stock = StockMarket(DataModel.items)
        cleaned_data = clean_data({
            "items": stock.get_current_prices()
        })  
        return JSONResponse(content=cleaned_data) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/yahoo/currency", response_model=ResponseModel)
@cache(expire=60 * 12)
async def get_country_price(DataModel:DataModel):
    try:
        country_currency = CountryCurrency(DataModel.items)
        cleaned_data = clean_data({
            "items": country_currency.get_current_prices()
        })  
        return JSONResponse(content=cleaned_data) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/yahoo/oil",response_model=ResponseModel)
@cache(expire=60 * 12)
async def get_oil_price(DataModel:DataModel):
    try:
        oil = OilMarket(DataModel.items)
        cleaned_data = clean_data({
            "items": oil.get_current_prices()
        })  
        return JSONResponse(content=cleaned_data) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get-items/stock",response_model=ResponseModel)
@cache(expire=60 * 30)
async def get_item_list_stock():
    try:
        stock_item = StockItem()
        return JSONResponse(content={
            'items' : stock_item.getItem(),
            'key': "sotck_market"
        }) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get-items/crypto",response_model=ResponseModel)
@cache(expire=60 * 30)
async def get_item_list_crypto():
    try:
        stock_item = CryptoItem()
        return JSONResponse(content={
            'items' : stock_item.getItem(),
            'key': "crypto_market"
        }) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get-items/oil",response_model=ResponseModel)
@cache(expire=60 * 30)
async def get_item_list_oil():
    try:
        oil = OilItem()
        return JSONResponse(content={
            'items' : oil.getItem(),
            'key': "oil_market"
        }) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get-items/currency",response_model=ResponseModel)
@cache(expire=60 * 30)
async def get_item_list_currency():
    try:
        stock_item = CurrencyItem()
        return JSONResponse(content={
            'items' : stock_item.getItem(),
            'key': "currency_market"
        }) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/get_historical_data")
async def fetch_historical_data(request: HistoricalDataRequest):
    symbols = request.symbols
    start_date = request.start_date
    end_date = request.end_date
    interval = request.interval

    result = get_historical_data(symbols, start_date, end_date, interval)

    return result