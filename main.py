import pandas as pd
import numpy as np
import pandas_ta as ta
import alpaca_trade_api as tradeapi
from backtrader import Cerebro, feeds, Strategy
from datetime import datetime, timedelta
import time

API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'
BASE_URL = 'https://paper-api.markets' 

