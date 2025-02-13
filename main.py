import pandas as pd
import numpy as np
import pandas_ta as ta
from kiteconnect import KiteConnect
from backtrader import Cerebro, feeds, Strategy
from datetime import datetime, timedelta
import time

# Zerodha Kite API credentials
API_KEY = 'your_api_key'
ACCESS_TOKEN = 'your_access_token'

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)

#Fetch historical data
def fetch_historical_data(symbol, start_date, end_date, timeframe='day'):
    data = kite.historical_data(instrument_token=symbol, from_date=start_date, to_date=end_date, interval=timeframe)
    data = pd.DataFrame(data)
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)
    return data
