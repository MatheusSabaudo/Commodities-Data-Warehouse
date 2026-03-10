# Dependencies
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Locals

commodities = ['CL=F', 'GC=F', 'SI=F']

def GetCommodities(symbol, period='5d', interval='1d'):
    ticker = yf.Ticker('CL=F')
    dataframe = ticker.history(period=period, interval=interval)[['Close']]
    dataframe['symbol'] = symbol
    return dataframe

def JoinCommodities(commodities):
    data = []
    for symbol in commodities:
        dataframe = GetCommodities(symbol)
        data.append(dataframe)
    return pd.concat(data) 

if __name__ == "__main__":
    joinedData = JoinCommodities(commodities)

# API Request

# Join commodities

# Connection to DB
