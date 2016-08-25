# class03pd38.py

# This script should mimic the SQL listed below:

# -- GROUP BY
# CREATE TABLE prices4 AS 
# SELECT
# extract(year from cdate) yr
# ,cdate
# ,closep
# FROM prices
# WHERE extract(year from cdate) > 1999;
# 
# SELECT yr, COUNT(yr) FROM prices4 GROUP BY yr;
# 
# -- GROUP BY ORDER BY
# SELECT yr, COUNT(yr) FROM prices4 GROUP BY yr ORDER BY yr;
# SELECT yr, COUNT(yr) FROM prices4 GROUP BY yr ORDER BY COUNT(yr);

# SQL lacks the ability to get data from the web.
# Pandas can get data from the web:

import pandas as pd
from datetime import datetime

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','volume','adjp']

# Mimic
# CREATE TABLE prices4 AS 
# SELECT
# extract(year from cdate) yr
# ,cdate
# ,closep
# FROM prices
# WHERE extract(year from cdate) > 1999;

extract_sr          = pd.to_datetime(prices_df.cdate_s)
pred_sr             = extract_sr.dt.year > 1999
prices4_df          = prices_df.copy()[pred_sr]
prices4_df['cdate'] = pd.to_datetime(prices4_df.cdate_s)
prices4_df['yr']    = prices4_df.cdate.dt.year
prices4_df          = prices4_df[['yr','cdate','closep']]

# I should report:
print(prices4_df.head())

# Mimic
# SELECT yr, COUNT(yr) FROM prices4 GROUP BY yr;

yr_df         = prices4_df[['yr','yr']]
yr_df.columns = ['yr','yrcount']
yr_gb         = yr_df.groupby('yr')

yr_gb_df = yr_gb.aggregate(len)
print(yr_gb_df)

'bye'
