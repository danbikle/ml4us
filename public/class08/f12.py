# f12.py

# This script should generate features from csv data.

import pandas as pd

f10_df = pd.read_csv('fx3/eur.csv', names=['ts','cp'])

slopes_a = [2,3,4,5,6,7,8,9]

# I should compute dependent variable, piplead:
f10_df['piplead'] = (10000.0*(f10_df.cp.shift(-1) - f10_df.cp) / f10_df.cp).fillna(0)
print(f10_df.head())

# I should compute mvgavg-slope for each slope_i

# ref:
# http://www.ml4.us/cclasses/class03pd41
# http://pandas.pydata.org/pandas-docs/stable/computation.html#rolling-windows
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling

for slope_i in slopes_a:
  rollx          = f10_df.rolling(window=slope_i)
  col_s          = 'slope'+str(slope_i)
  slope_sr       = 10000.0 * (rollx.mean().cp - rollx.mean().cp.shift(1))/rollx.mean().cp
  f10_df[col_s] = slope_sr
print(f10_df.tail())

# I should write to CSV file to be used later:
f10_df.to_csv('fx3/feat.csv', float_format='%4.4f', index=False)

'bye'

