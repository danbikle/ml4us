"""
class03pd47.py

This script should slice and dice
"""

import pandas as pd
import numpy  as np

prices_df = pd.read_csv('http://ml4.us/csv/GSPC.csv')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','adjp','volume']

# I should get 2016 July and two columns:
pred_sr = (prices_df.cdate_s > '2016-07') & (prices_df.cdate_s < '2016-08')
s1_df   = prices_df[pred_sr][['cdate_s','closep']]
print(s1_df)

# I should do it the numpy way:
prices_a = np.array(prices_df)

# I should get all rows where column-0 > '2016-07'
pred1_a  = (prices_a[:,0] > '2016-07')
# I should get all rows where column-0 < '2016-08'
pred2_a  = (prices_a[:,0] < '2016-08')

# I should combine the two predicates:
preds_a = pred1_a & pred2_a

# I should slice out july:
july_a   = prices_a[preds_a]

# I should get all rows and get columns 0 and 4:
s1_a     = july_a[:,[0,4]]
print(s1_a)

'bye'
