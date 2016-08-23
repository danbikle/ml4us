# class03pd10.py

# This script should mimic the SQL listed below:

# SELECT COUNT(cdate) FROM prices;
# SELECT COUNT(lowp)  FROM prices;
# SELECT COUNT(*)     FROM prices;
# SELECT MIN(cdate),MIN(closep),MIN(volume) FROM prices;
# SELECT MAX(closep),MAX(volume), AVG(closep),AVG(volume) FROM prices;

# SQL lacks the ability to get data from the web.
# Pandas can get data from the web:

import pandas as pd
import pdb

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
pdb.set_trace()
prices_df.head()

'bye'

