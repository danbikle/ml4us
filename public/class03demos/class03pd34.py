"""
class03pd34.py

This script should mimic the SQL listed below:

-- Delete a row:
DELETE FROM prices3 WHERE cdate = '2016-08-10';

-- Delete some rows:
DELETE FROM prices3 WHERE cdate < '2016-08-10';

-- Delete all rows:
SELECT COUNT(*) FROM prices3; 
DELETE          FROM prices3;
SELECT COUNT(*) FROM prices3; 
"""

# SQL lacks the ability to get data from the web.
# Pandas can get data from the web:

import pandas as pd

prices_df         = pd.read_csv('http://ml4.us/csv/ibm.csv')
prices_df.columns = ['cdate_s', 'openp', 'highp', 'lowp', 'closep', 'adjp', 'volume']

# I should setup prices3_df:
pred1a_sr  = prices_df.cdate_s > '2016-08-08'
pred1b_sr  = prices_df.cdate_s < '2016-09-01'
pred1_sr   = (pred1a_sr & pred1b_sr)
prices3_df = prices_df.copy()[['cdate_s','openp']][pred1_sr]

# I should report:
print(prices3_df)

# Mimic
# DELETE FROM prices3 WHERE cdate = '2016-08-10';

row_sr      = ( prices3_df.cdate_s == '2016-08-10')
prices3_loc =   prices3_df.loc[row_sr]
prices3_df  =   prices3_df.drop(prices3_loc.index)

# I should report:
print(prices3_df)

# Mimic
# DELETE FROM prices3 WHERE cdate < '2016-08-10';

rows_sr     = ( prices3_df.cdate_s < '2016-08-10')
prices3_loc =   prices3_df.loc[rows_sr]
prices3_df  =   prices3_df.drop(prices3_loc.index)

# I should report:
print(prices3_df)

# Mimic
# -- Delete all rows:
# DELETE FROM prices3;

prices3_df = prices3_df.drop(prices3_df.index)

# I should report:
print(prices3_df)

'bye'
