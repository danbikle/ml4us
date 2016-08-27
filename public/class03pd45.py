# class03pd45.py

# This script should slice and dice

import pandas as pd

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','volume','adjp']

s1_df = prices_df[['cdate_s','closep']][5:11]
import pdb
pdb.set_trace()
s1_df

s2_df = prices_df[5:11][['cdate_s','closep']]
s2_df


'bye'
