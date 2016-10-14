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
gspc_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')[['Date','Close']]
gspc_df.columns = ['cdate','cp']

# I should compute pctlead:
gspc_df['pctlead'] = (100.0 * (gspc_df.cp.shift(-1) - gspc_df.cp) / gspc_df.cp).fillna(0)

# ref:
# http://www.ml4.us/cclasses/class03pd41
# http://pandas.pydata.org/pandas-docs/stable/computation.html#rolling-windows
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling

# I should declare which price-based, mvgavg-slope features I want:
slopes_a  = [2,3,4,5,6,7,8,9]

for slope_i in slopes_a:
  rollx          = gspc_df.rolling(window=slope_i)
  col_s          = 'slope'+str(slope_i)
  slope_sr       = 100.0 * (rollx.mean().cp - rollx.mean().cp.shift(1))/rollx.mean().cp
  gspc_df[col_s] = slope_sr

'bye'
  
