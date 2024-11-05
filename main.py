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

@app.post("/yahoo/country", response_model=ResponseModel)
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
