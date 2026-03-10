# Dependencies
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Locals

load_dotenv()

commodities = ['CL=F', 'GC=F', 'SI=F']

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

# API Request

def GetCommodities(symbol, period='5d', interval='1d'):
    ticker = yf.Ticker(symbol)
    dataframe = ticker.history(period=period, interval=interval)[['Close']]
    dataframe['symbol'] = symbol
    return dataframe

# Join commodities

def JoinCommodities(commodities):
    data = []
    for symbol in commodities:
        dataframe = GetCommodities(symbol)
        data.append(dataframe)
    return pd.concat(data) 

# Connection to DB

def ExportData(df, schema=DB_SCHEMA):
    df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)

if __name__ == "__main__":
    joinedData = JoinCommodities(commodities)
    ExportData(joinedData, schema='public')