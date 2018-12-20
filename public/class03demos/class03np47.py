"""
class03np47.py

This script should filter a month of rows from prices_a.
And it should get only columns 0 and 4.

Demo:
python class03np47.py
"""

import pandas as pd
import numpy  as np

prices_df = pd.read_csv('https://ml4.herokuapp.com/csv/GSPC.csv')

# I should do it the numpy way:
prices_a = np.array(prices_df)

# I should get all rows where column-0 > '2016-07'
pred1_a = (prices_a[:,0] > '2016-07')
# I should get all rows where column-0 < '2016-08'
pred2_a = (prices_a[:,0] < '2016-08')

# I should combine the two predicates:
preds_a = pred1_a & pred2_a

# I should slice out july:
july_a = prices_a[preds_a]

# I should get all rows and get columns 0 and 4:
s1_a = july_a[:,[0,4]]
print(s1_a)

'bye'
