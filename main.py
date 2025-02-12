import pandas as pd
import numpy as np
import pandas_ta as ta
import alpaca_trade_api as tradeapi
from backtrader import Cerebro, feeds, Strategy
from datetime import datetime, timedelta
import time