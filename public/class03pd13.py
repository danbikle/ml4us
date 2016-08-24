# class03pd13.py

# This script should mimic the SQL listed below:

# SELECT * FROM prices WHERE cdate = (SELECT MAX(cdate) FROM prices);              
# SELECT cdate,closep FROM prices WHERE cdate = (SELECT MAX(cdate)-1 FROM prices);
# SELECT cdate,closep FROM prices WHERE cdate > (SELECT MAX(cdate)-10 FROM prices);

import pandas as pd
import numpy  as np
from datetime import datetime
import pdb

# SQL lacks the ability to get data from the web.
# Pandas can get data from the web:

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','volume','adjp']

# Mimic
# SELECT * FROM prices WHERE cdate = (SELECT MAX(cdate) FROM prices);

prices_df['cdate'] = pd.to_datetime(prices_df.cdate_s)
arg_max_cdate      = prices_df.cdate.argmax()
print(prices_df.iloc[arg_max_cdate])

# Mimic
# SELECT cdate,closep FROM prices WHERE cdate = (SELECT MAX(cdate)-1 FROM prices);

from datetime import timedelta
maxdate   = prices_df.iloc[arg_max_cdate].cdate
maxdate_1 = maxdate - timedelta(days=1)
pred_sr   = (prices_df.cdate == maxdate_1)
myrow     = prices_df[['cdate','closep']][pred_sr]
print(myrow)

'bye'

