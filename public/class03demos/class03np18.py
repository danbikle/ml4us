"""
class03np18.py

This script should compute columns pctlag1 and pctlead from closep.

Demo:
python class03np18.py
"""

import pandas as pd
import numpy  as np

prices_df = pd.read_csv('https://ml4.herokuapp.com/csv/GSPC.csv')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','adjp','volume']

# I should get 2016 July and two columns.
# I should do it the numpy way:
prices_a = np.array(prices_df)

# I should get all rows where column-0 > '2016-07'
pred1_a  = (prices_a[:,0] > '2016-07')
# I should get all rows where column-0 < '2016-08'
pred2_a  = (prices_a[:,0] < '2016-08')

# I should slice out july:
july_a   = prices_a[pred1_a & pred2_a]

# I should get all rows and get columns 0 and 4:
s1_a      = july_a[:,[0,4]]
# I should create a column of closing prices:
cp_a      = s1_a[:,[1]]
# 0th closing price:
elem0     = cp_a[:1]
# last cp:
elem_last = cp_a[-1:]
# duplicate elem_last at the end:
lead_a    = np.vstack((cp_a , elem_last))
# duplicate elem0 at the start:
lag1_a    = np.vstack((elem0, cp_a     ))
# Easy calculations:
pctlag1   = 100 * ( cp_a - lag1_a[:-1] ) / lag1_a[:-1] 
pctlead   = 100 * ( lead_a[1:] - cp_a) / cp_a
# I should do what the Pandas script did:
s1_a      = np.hstack((s1_a,pctlag1))
s1_a      = np.hstack((s1_a,pctlead))

# I should visualize:
print(s1_a)

'bye'
