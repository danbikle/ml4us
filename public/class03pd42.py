# class03pd42.py

# This script should mimic the SQL listed below:

# -- Window Functions (5 Day Moving Average)
# CREATE TABLE prices5 AS 
# SELECT
# cdate
# ,closep
# ,AVG(closep)OVER(ORDER BY cdate ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) mvgavg5day
# FROM prices
# WHERE cdate > '2016-08-01'
# ORDER BY cdate;
# 
# SELECT * FROM prices5 WHERE cdate BETWEEN '2016-08-01' AND '2016-08-31' ORDER BY cdate;

# SQL lacks the ability to get data from the web.
# Pandas can get data from the web:

import pandas as pd

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','volume','adjp']

pred_sr = (prices_df.cdate_s > '2016-08-01')
prices5_df = prices_df[['cdate_s','closep']][pred_sr].sort_values(by=['cdate_s'])
myr = prices5_df.rolling(window=5)
prices5_df['mvgavg5day'] = myr.mean().closep

pred2_sr = (prices5_df.cdate_s >= '2016-08-01') & (prices5_df.cdate_s <= '2016-08-31')
print(prices5_df[pred2_sr].sort_values(by=['cdate_s']))
'bye'
