# class03pd29.py

# This script should mimic the SQL listed below:

# -- Update some rows of a column:
# UPDATE prices3 SET diff = 1 WHERE cdate = '2016-08-10';
# 
# -- Update column using other columns:
# UPDATE prices3 SET diff = closep - openp;

# SQL lacks the ability to get data from the web.
# Pandas can get data from the web:

import pandas as pd

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','volume','adjp']

# I should setup prices3:
pred1_sr   = prices_df.cdate_s > '2016-08-08'
prices3_df = prices_df.copy()[['cdate_s','openp','closep']][pred1_sr]
prices3_df['diff'] = prices3_df.closep - prices3_df.openp

# Mimic
# UPDATE prices3 SET diff = 1 WHERE cdate = '2016-08-10';

row_sr = (prices3_df.cdate_s == '2016-08-10')
prices3_df.loc[row_sr, 'diff'] = 1

# I should report:
print(prices3_df)

'bye'
