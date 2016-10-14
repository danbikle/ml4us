# keras14.py

# This script should classify observations of S&P500 one-day percent gain.
# The two classes are above average and below average.
# Demo:
# ./keras_theano.bash keras14.py

import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import pandas as pd
import numpy  as np
import pdb

# I should get prices:
data_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')[['Date','Close']]
data_df.columns = ['cdate','cp']

# I should compute pctlead:
data_df['pctlead'] = (100.0 * (data_df.cp.shift(-1) - data_df.cp) / data_df.cp).fillna(0)

# ref:
# http://www.ml4.us/cclasses/class03pd41
# http://pandas.pydata.org/pandas-docs/stable/computation.html#rolling-windows
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling

# I should declare which price-based, mvgavg-slope features I want:
slopes_a  = [2,3,4,5,6,7,8,9]

for slope_i in slopes_a:
  rollx          = data_df.rolling(window=slope_i)
  col_s          = 'slope'+str(slope_i)
  slope_sr       = 100.0 * (rollx.mean().cp - rollx.mean().cp.shift(1))/rollx.mean().cp
  data_df[col_s] = slope_sr

# I should generate Date features:
dt_sr = pd.to_datetime(data_df.cdate)
dow_l = [float(dt.strftime('%w' ))/100.0 for dt in dt_sr]
moy_l = [float(dt.strftime('%-m'))/100.0 for dt in dt_sr]
data_df['dow'] = dow_l
data_df['moy'] = moy_l

'bye'
  
