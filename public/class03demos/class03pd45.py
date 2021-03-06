"""
class03pd45.py

This script should demonstrate flexibility to locate iloc[]
when I want to slice and dice.

Demo:
python class03pd45.py
"""

import pandas as pd
import numpy  as np

prices_df = pd.read_csv('https://ml4.herokuapp.com/csv/GSPC.csv')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','adjp','volume']

# I should get 2 columns and rows 5 through 11:
s1_df = prices_df[['cdate_s','closep']].iloc[5:11]
print(s1_df)

# I do same as above but in different order.
# I should get rows 5 through 11 and 2 columns:
s2_df = prices_df.iloc[5:11][['cdate_s','closep']]
print(s2_df)
# s1_df and s2_df should have same data.

'bye'
