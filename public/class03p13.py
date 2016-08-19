# class03p13.py

# This script should use Linear Algebra to find beta of a fitted line.
# ref:
# http://www.stat.purdue.edu/~jennings/stat514/stat512notes/topic3.pdf
# 
import pandas as pd
import numpy  as np

csvfile   = 'http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC'
cp_df     = pd.read_csv(csvfile).sort_values(['Date'])
cp2016_sr = (cp_df.Date > '2016') & (cp_df.Date < '2017')
cp2016_df = cp_df[['Date','Close']][cp2016_sr]

'bye'
