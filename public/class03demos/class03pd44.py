"""
class03pd44.py

This script should sort df by cdate
"""

import pandas as pd

prices_df = pd.read_csv('https://ml4.herokuapp.com/csv/GSPC.csv')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','adjp','volume']

prices_df = prices_df.sort_values(by=['cdate_s'])

print(prices_df.head())

'bye'
