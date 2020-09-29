import sys
sys.path.append('../')
from market_regime.market_regime_detection import Market_regime as mrd
import datetime
from pandas_datareader import DataReader


secs = ['SPY']
data = DataReader(secs, 'yahoo', '2017-01-01',
                  str(datetime.date.today()))['Adj Close']
MR = mrd(data).directional_change_fit().markov_switching_regression_fit().hidden_markov_model_fit()
MR.plot_market_regime(day_interval=20, plot_hmm=True)
MR.data.info()

