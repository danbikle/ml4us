"""
genf.py

This script should generate feat.csv from GSPC.csv

The file, feat.csv, is full of machine learning features.

We have two types of features:
  - price features
  - date features

Demo:
~/anaconda3/bin/python genf.py
"""

import pdb
import pandas as pd
import numpy  as np

# I should get prices 
prices_df       = pd.read_csv('GSPC.csv')
feat_df         = prices_df[['Date','Close']].sort_values(['Date'])
feat_df.columns = ['cdate','closep']
pctlead_sr      = (100.0*(feat_df.closep.shift(-1)-feat_df.closep)/feat_df.closep).fillna(0)
feat_df['pctlead'] = np.round(pctlead_sr,3)
feat_df['updown']  = [int(pctlead > 0.0) for pctlead in feat_df.pctlead]

# I should calculate pctlags:
lags_l = [1,2,3,4,5,6,7,8,12,16]
for lag_i in lags_l:
  pctlagx_sr = (100.0*(feat_df.closep - feat_df.closep.shift(lag_i))/feat_df.closep.shift(lag_i)).fillna(0)
  col_s      = 'pctlag'+str(lag_i)
  feat_df[col_s] = np.round(pctlagx_sr,4)
# I should calculate mvg-avg slopes:
slopes_l = [2,3,4,5,6,7,8,9]
for slope_i in slopes_l:
  rollx          = feat_df.rolling(window=slope_i)
  col_s          = 'slope'+str(slope_i)
  slope_sr       = 100.0 * (rollx.mean().closep - rollx.mean().closep.shift(1))/rollx.mean().closep
  feat_df[col_s] = np.round(slope_sr,4)
# I should generate Date features:
dt_sr = pd.to_datetime(feat_df.cdate)
dow_l = [float(dt.strftime('%w' ))/100.0 for dt in dt_sr]
moy_l = [float(dt.strftime('%-m'))/100.0 for dt in dt_sr]
feat_df['dow'] = dow_l
feat_df['moy'] = moy_l

feat_df.to_csv('feat.csv', float_format='%4.4f', index=False)

'bye'

