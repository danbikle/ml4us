# class0310.py

# Use Pandas to plot prices of GSPC for 2016.
# Plot a straight line from first price to last price.
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
from datetime import datetime

csvfile = 'http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC'
# Goog: In pandas how to sort a dataframe?
cp_df     = pd.read_csv(csvfile).sort_values(['Date'])
# Goog: In pandas how to filter?
cp2016_sr = (cp_df.Date > '2016') & (cp_df.Date < '2017')
cp2016_df = cp_df[['Date','Close']][cp2016_sr]

# Algebra and Geometry say a line is described by
# y = mx + b
# m, the slope is (y1-y0)/(x1-x0)
# and b is the y intercept.
m_f = (cp2016_df.iloc[-1].Close-cp2016_df.iloc[0].Close) / len(cp2016_df)
b_f = cp2016_df.iloc[0].Close
pdb.set_trace()

# I should collect points to plot straight line:
sl_l = [ (m_f * x_i + b_f) for x_i in range(len(cp2016_df))]
sl_l
cp2016_df['sl'] = sl_l
# Goog: In pandas how to convert column into index?
cpdate2016_df = cp2016_df.set_index(['Date'])
# Goog: In pandas how to plot?
cpdate2016_df.plot.line(title="GSPC 2016")
plt.show()

'bye'
