# class0313.py

# Use Pandas to plot prices of GSPC for 2016.
# Plot a straight line from first price to last price.
# Calculate RMSE for that line.
# Use Linear Algebra to fit a line to GSPC 2016 price points.

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

# I should collect points to plot straight line:
sl_l = [ (m_f * x_i + b_f) for x_i in range(len(cp2016_df))]

# Add the points to the DataFrame:
cp2016_df['sl'] = sl_l

# Calculate squared errors:
cp2016_df['sqe'] = (cp2016_df.Close - cp2016_df.sl)**2
# Goog: How to calculate Root Mean Square of Errors?
rmse_f = np.sqrt(np.mean(cp2016_df.sqe))
print(rmse_f)

# Goog: How to Use Linear Algebra to fit a line
# ref:
# http://www.stat.purdue.edu/~jennings/stat514/stat512notes/topic3.pdf
# It says:
# yhat = x_input *( inverse(xvals_a.T * xvals_a) * xvals_a.T * yvals_a )
# I need to convert above expression into Numpy.

# I start by seeing the X-values as simple integers starting at 0:
x_a     = np.array(range(len(cp2016_df))).reshape((len(cp2016_df),1))
# Notice that I reshaped it into a column.
# Above pdf asks me to pre-pend a column vector of ones:
ones_l  = [1]*len(cp2016_df)
ones_a  = np.array(ones_l).reshape((len(cp2016_df),1))
# I should build xvals_a from column of ones then integers:
xvals_a = np.hstack((ones_a,x_a))
# I should transform the prices into a column vector of y-values:
yvals_a = np.array(cp2016_df.Close).reshape((len(cp2016_df),1))
# I have X and Y, now implement Linear Algebra with NumPy:
middle_a = np.linalg.pinv(np.matmul(xvals_a.T,xvals_a))
rhs_a    = np.matmul(xvals_a.T,yvals_a)
b_a      = np.matmul(middle_a,rhs_a)

# To get some values of the straight line, I will use xvals_a as x_input
x_input = xvals_a
yhat    = np.matmul(x_input,b_a)
# I should add yhat to df so I can visualize the fit:
cp2016_df['yhat'] = yhat


date_cp_sl_yhat_df = cp2016_df[['Date','Close','sl','yhat']]
cp_sl_yhat_df      = date_cp_sl_yhat_df.set_index(['Date'])

# I should plot
cp_sl_yhat_df.plot.line(title="GSPC 2016")
plt.show()

'bye'
