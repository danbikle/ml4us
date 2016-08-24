# class03pd26.py

# This script should mimic the SQL listed below:

# -- Copy rows from table to table:
# INSERT INTO prices3
# SELECT cdate,openp,closep, closep - openp AS diff FROM prices
# WHERE cdate = '2016-08-01';
# 
# -- Copy rows from table to table2 where rows not in table2 already:
# INSERT INTO prices3
# SELECT cdate,openp,closep, closep - openp AS diff FROM prices
# WHERE  cdate BETWEEN '2016-08-01' AND '2016-08-31'
# AND    cdate NOT IN (SELECT cdate FROM prices3);
# 
# -- Update all rows of a column:
# UPDATE prices3 SET diff = 0;

# SQL lacks the ability to get data from the web.
# Pandas can get data from the web:

import pandas as pd
from datetime import datetime, timedelta

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','volume','adjp']

# I should setup prices3:
pred1_sr   = prices_df.cdate_s > '2016-08-08'
prices3_df = prices_df.copy()[['cdate_s','openp','closep']][pred1_sr]
prices3_df['diff'] = prices3_df.closep - prices3_df.openp

# Mimic
# INSERT INTO prices3
# SELECT cdate,openp,closep, closep - openp AS diff FROM prices
# WHERE cdate = '2016-08-01';

import pdb
pdb.set_trace()

pred2_sr       = prices_df.cdate_s == '2016-08-01'
tmp_df         = prices_df.copy()[['cdate_s','openp','closep']][pred2_sr]
tmp_df['diff'] = tmp_df.closep - tmp_df.openp
prices4_df     = pd.concat((prices3_df,tmp_df))

'bye'
