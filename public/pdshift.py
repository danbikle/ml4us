
import pandas as pd
import numpy  as np

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_df.columns = ['cdate_s','openp','highp','lowp','closep','volume','adjp']

# I should get 2016 July and two columns:
pred_sr = (prices_df.cdate_s > '2016-07') & (prices_df.cdate_s < '2016-08')
s1_df   = prices_df[pred_sr][['cdate_s','closep']]
print(s1_df)

import pdb
pdb.set_trace()

# vis a push-down so top row becomes NaN:
s2_df = s1_df.shift(1)
s2_df

# this work:
s3_df = s1_df.shift(-1)
s3_df

'bye'
