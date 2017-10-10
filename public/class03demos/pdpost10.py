# pdpost10.py

# This script should copy gspc prices from web into a Postgres table.

import pandas as pd

prices_df = pd.read_csv('http://tkrprice.herokuapp.com/static/gspc.csv')

prices_df.columns = ['cdate','openp','highp','lowp','closep','adjp','volume']

# Ref:
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_sql.html
# http://docs.sqlalchemy.org/en/latest/core/engines.html#postgresql

# I should use sqlalchemy to connect to madlib role in Postgres:

from sqlalchemy import create_engine
engine = create_engine('postgresql://madlib:madlib@127.0.0.1:5432/madlib')

# I should write to a table named prices:
prices_df.to_sql('prices',engine, index=False, if_exists='replace')

# I should read from a table named prices:
sql_s      = 'select * from prices order by cdate;'
prices2_df = pd.read_sql(sql_s,engine,parse_dates=['cdate'])
print(prices2_df.tail())

'bye'
