# class03pd13.py

# This script should mimic the SQL listed below:

# SELECT * FROM prices WHERE cdate = (SELECT MAX(cdate) FROM prices);              
# SELECT cdate,closep FROM prices WHERE cdate = (SELECT MAX(cdate)-1 FROM prices);
# SELECT cdate,closep FROM prices WHERE cdate > (SELECT MAX(cdate)-10 FROM prices);

import pandas as pd
import numpy  as np
from datetime import datetime

# SQL lacks the ability to get data from the web.
# Pandas can get data from the web:

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','volume','adjp']

# Mimic
# SELECT * FROM prices WHERE cdate = (SELECT MAX(cdate) FROM prices);

prices_df['cdate'] = pd.to_datetime(prices_df.cdate_s)
max_sr = (prices_df.cdate == prices_df.cdate.max())
print(prices_df[max_sr])

# Mimic
# SELECT cdate,closep FROM prices WHERE cdate = (SELECT MAX(cdate)-1 FROM prices);

from datetime import timedelta
max_1_sr = (prices_df.cdate == (prices_df.cdate.max() - timedelta(days=1)))
myrow    = prices_df[['cdate','closep']][max_1_sr]
print(myrow)

# Mimic
# SELECT cdate,closep FROM prices WHERE cdate > (SELECT MAX(cdate)-10 FROM prices);

max_10_sr = (prices_df.cdate > (prices_df.cdate.max() - timedelta(days=10)))
myrows    = prices_df[['cdate','closep']][max_10_sr]
print(myrows)

'bye'

