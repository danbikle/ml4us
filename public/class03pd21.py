# class03pd21.py

# This script should mimic the SQL listed below:

# SELECT max(closep)     FROM
#   (SELECT cdate,closep FROM prices WHERE cdate > (SELECT MAX(cdate)-10 FROM prices)) iv;
# 
# DROP   TABLE IF EXISTS prices2;
# CREATE TABLE prices2 AS SELECT cdate,openp,closep FROM prices WHERE cdate > '2016-08-08';
# 
# DROP   TABLE IF EXISTS prices3;
# CREATE TABLE prices3 AS SELECT cdate,openp,closep, closep - openp AS diff FROM prices2;

# SQL lacks the ability to get data from the web.
# Pandas can get data from the web:

import pandas as pd
from datetime import datetime, timedelta

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','volume','adjp']

# Mimic
# SELECT max(closep)     FROM
#   (SELECT cdate,closep FROM prices WHERE cdate > (SELECT MAX(cdate)-10 FROM prices)) iv;

# I should subtract 10days from max-cdate:
max_10    = pd.to_datetime(prices_df.cdate_s).max() - timedelta(days=10)
# I should create a predicate from max-cdate:
max_10_sr = (pd.to_datetime(prices_df.cdate_s) > max_10)
# I should apply the predicate, get closep from resulting df, get max from closep series:
max_cp    = prices_df[['cdate_s','closep']][max_10_sr].closep.max()
print(max_cp)

'bye'
