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
prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')[['Date','Close']]
prices_df.columns = ['cdate','cp']

# I should sort by cdate, ascending.
data_df = prices_df.copy().sort_values(by=['cdate'])

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

# I should split data_df into train_df and test_df
trainsize     = 25
testyear_i    = 2016
train_end_i   = testyear_i
train_end_s   = str(train_end_i)
train_start_i = train_end_i - trainsize
train_start_s = str(train_start_i)
# train and test observations should not overlap:
test_start_i  = train_end_i
test_start_s  = str(test_start_i)
test_end_i    = test_start_i+1
test_end_s    = str(test_end_i)

train_sr = (data_df.cdate > train_start_s) & (data_df.cdate < train_end_s)
test_sr  = (data_df.cdate > test_start_s)  & (data_df.cdate < test_end_s)
train_df = data_df[train_sr]
test_df  = data_df[test_sr]
# I should now have split data_df into train_df and test_df

import pdb
pdb.set_trace()
train_df.head()
train_df.tail()
# I should convert df to np-array:
x_train_a = np.array(train_df)[:,3:]
y_train_a = np.array(train_df.pctlead)


'bye'
  
