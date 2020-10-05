import sys
sys.path.append('../')
from market_regime.market_regime_detection import Market_regime as mrd
import datetime
import pandas as pd
from pandas_datareader import DataReader
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()


secs = ['SPY']
#data = pdr.get_data_yahoo('SPY', period='1y',interval="1d")
#data = pd.DataFrame(data['Adj Close'])
data = DataReader(secs, 'yahoo', '2020-01-01',
                 str(datetime.date.today()))['Adj Close']
MR = mrd(data, data_freq='D').directional_change_fit(dc_offset=[0.1,0.15])#.markov_switching_regression_fit().hidden_markov_model_fit()
MR.plot_market_regime(day_interval=20, no_markov=True)