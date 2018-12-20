"""
class03pd47.py

This script should slice and dice.

Demo:
python class03pd47.py
"""

import pandas as pd
import numpy  as np

prices_df = pd.read_csv('https://ml4.herokuapp.com/csv/GSPC.csv')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','adjp','volume']

# I should get 2016 July and two columns:
pred_sr = (prices_df.cdate_s > '2016-07') & (prices_df.cdate_s < '2016-08')
s1_df   = prices_df.loc[pred_sr][['cdate_s','closep']]
print(s1_df)

'bye'
