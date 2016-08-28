# class03pd45.py

# This script should slice and dice

import pandas as pd
import numpy  as np

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','volume','adjp']

# I should get 2 columns and rows 5 through 11:
s1_df = prices_df[['cdate_s','closep']][5:11]
print(s1_df)

# I do same as above but in different order.
# I should get rows 5 through 11 and 2 columns:
s2_df = prices_df[5:11][['cdate_s','closep']]
print(s2_df)
# s1_df and s2_df should have same data.

# I should do it the numpy way:
prices_a = np.array(prices_df)
s1_a = prices_a[5:11,[0,4]]
print(s1_a)
# Numpy is more constrained.
# I should specify rows first, columns second.

'bye'
