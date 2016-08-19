# class03p11.py

# This script should use Pandas to plot prices of GSPC for 2016.
# This script should Plot a straight line from first price to last price.

import pandas as pd
import matplotlib.pyplot as plt

csvfile   = 'http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC'
cp_df     = pd.read_csv(csvfile).sort_values(['Date'])
cp2016_sr = (cp_df.Date > '2016') & (cp_df.Date < '2017')
cp2016_df = cp_df[['Date','Close']][cp2016_sr]

# Algebra and Geometry say a line is described by
# y = mx + b
# m, the slope is (y1-y0)/(x1-x0):

# Useful concept:
# If I use integers (starting at 0) as X-values,
# then my syntax is simpler.

# (x1-x0) is:
x1x0_i = len(cp2016_df)
# (y1-y0) is:
y1y0_f = cp2016_df.iloc[-1].Close-cp2016_df.iloc[0].Close

# m, the slope is (y1-y0)/(x1-x0):
m_f = y1y0_f / x1x0_i
# And b is the y intercept:
b_f = cp2016_df.iloc[0].Close

# My equation for straight line:
def yval(x_in):
    return m_f * x_in + b_f

# I should collect points to plot straight line:
yvals_l = [ yval(x_i) for x_i in range(len(cp2016_df))]

# Add the points to the DataFrame:
cp2016_df['sl'] = yvals_l

# I should plot
cpdate2016_df = cp2016_df.set_index(['Date'])
cpdate2016_df.plot.line(title="GSPC 2016")
plt.show()

'bye'
