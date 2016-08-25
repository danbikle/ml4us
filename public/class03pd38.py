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
import pdb
pdb.set_trace()

extract_sr = pd.to_datetime(prices_df.cdate_s)
pred_sr = extract_sr.year > 1999
prices4_df = prices_df.copy()[['cdate_s','closep']]

pdb.set_trace()

'bye'
