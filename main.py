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