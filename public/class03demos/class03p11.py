"""
class03p11.py

This script should use Pandas to plot prices of GSPC for 2016.
This script should Plot a straight line from first price to last price.

Demo:
python class03p10.py
"""

import pandas as pd
import matplotlib.pyplot as plt

csvfile_s = 'http://spy611.herokuapp.com/csv/allpredictions.csv'
cp_df     = pd.read_csv(csvfile_s).sort_values(['cdate'])
cp2016_sr = (cp_df.cdate > '2016') & (cp_df.cdate < '2017')
cp2016_df = cp_df[['cdate','cp']][cp2016_sr]

# Algebra and Geometry say a line is described by
# y = mx + b
# m, the slope is (y1-y0)/(x1-x0):

# Useful concept:
# If I use integers (starting at 0) as X-values,
# then my syntax is simpler.

# (x1-x0) is:
# x1x0_i = len(cp2016_df)
# Should be faster, better way:
x1x0_i = cp2016_df.index.size

# (y1-y0) is:
y1y0_f = cp2016_df.iloc[-1].cp-cp2016_df.iloc[0].cp

# m, the slope is (y1-y0)/(x1-x0):
m_f = y1y0_f / x1x0_i
# And b is the y intercept:
b_f = cp2016_df.iloc[0].cp

# My equation for straight line:
def yval(x_in):
    return m_f * x_in + b_f

# I should collect points to plot straight line:
# yvals_l = [ yval(x_i) for x_i in range(len(cp2016_df))]
yvals_l = [ yval(x_i) for x_i in range(x1x0_i) ]

# Add the points to the DataFrame:
cp2016_df['sl'] = yvals_l

# To make a better plot I should convert X-values from integers to series of strings:
cpdate2016_df = cp2016_df.set_index(['cdate'])
# I should plot cp (closing price), and straight line:
cpdate2016_df.plot.line(title="GSPC 2016")
plt.show()

'bye'
