# class03pd45.py

# This script should slice and dice

import pandas as pd
import numpy  as np

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','volume','adjp']

# I should get 2016 July and two columns:
pred_sr = (prices_df.cdate_s > '2016-07') & (prices_df.cdate_s < '2016-08')
s1_df   = prices_df[pred_sr][['cdate_s','closep']]
print(s1_df)
import pdb
pdb.set_trace()

# I should do it the numpy way:
prices_a = np.array(prices_df)
pred_a   = (prices_a[:,0] > '2016-07') & (prices_a[:,0] < '2016-08')
s1_a     = prices_a[pred_a,[0,4]]
print(s1_a)

'bye'
