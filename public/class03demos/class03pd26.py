"""
class03pd26.py

This script should mimic the SQL listed below:

-- Copy rows from table to table:
INSERT INTO prices3
SELECT cdate,openp,closep, closep - openp AS diff FROM prices
WHERE cdate = '2016-08-01';

-- Copy rows from table to table2 where rows not in table2 already:
INSERT INTO prices3
SELECT cdate,openp,closep, closep - openp AS diff FROM prices
WHERE  cdate BETWEEN '2016-08-01' AND '2016-08-31'
AND    cdate NOT IN (SELECT cdate FROM prices3);

-- Update all rows of a column:
UPDATE prices3 SET diff = 0;
"""

# SQL lacks the ability to get data from the web.
# Pandas can get data from the web:

import pandas as pd

prices_df         = pd.read_csv('https://ml4.herokuapp.com/csv/ibm.csv')
prices_df.columns = ['cdate_s', 'openp', 'highp', 'lowp', 'closep', 'adjp', 'volume']

# I should setup prices3:
pred1a_sr  = prices_df.cdate_s > '2016-08-08'
pred1b_sr  = prices_df.cdate_s < '2016-09-01'
pred1_sr   = (pred1a_sr & pred1b_sr)
prices3_df = prices_df.copy()[['cdate_s','openp','closep']][pred1_sr]
prices3_df['diff'] = prices3_df.closep - prices3_df.openp

# Mimic
# INSERT INTO prices3
# SELECT cdate,openp,closep, closep - openp AS diff FROM prices
# WHERE cdate = '2016-08-01';

pred2_sr       = prices_df.cdate_s == '2016-08-01'
tmp_df         = prices_df.copy()[['cdate_s','openp','closep']][pred2_sr]
tmp_df['diff'] = tmp_df.closep - tmp_df.openp
prices3_df     = pd.concat((prices3_df,tmp_df))

# I should report:
print(prices3_df.sort_values(['cdate_s']))

# Mimic
# -- Copy rows from table to table2 where rows not in table2 already:
# INSERT INTO prices3
# SELECT cdate,openp,closep, closep - openp AS diff FROM prices
# WHERE  cdate BETWEEN '2016-08-01' AND '2016-08-31'
# AND    cdate NOT IN (SELECT cdate FROM prices3);

# I should create the first predicate:
pred_first_sr = (prices_df.cdate_s >= '2016-08-01') & (prices_df.cdate_s <= '2016-08-31')
# I should create the 2nd predicate:
pred_isin_sr  = prices_df.cdate_s.isin(prices3_df.cdate_s)

pred_notin_sr = ~pred_isin_sr # Similar to NOT IN syntax in SQL

# I should create the 3rd predicate:
pred3_sr = pred_first_sr & pred_notin_sr
# I should apply the predicate
insert_these_df = prices_df.copy()[['cdate_s','openp','closep']][pred3_sr]
# I should create the diff-column
insert_these_df['diff'] = insert_these_df.closep - insert_these_df.openp
# I should do the insert:
prices3_df              = pd.concat((prices3_df,insert_these_df))

# I should report:
print(prices3_df.sort_values(['cdate_s']))

# Mimic
# UPDATE prices3 SET diff = 0;

prices3_df['diff'] = 0

# I should report:
print(prices3_df.sort_values(['cdate_s']))

'bye'
