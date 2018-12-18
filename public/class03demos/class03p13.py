"""
class03p13.py

This script should use Linear Algebra to find w of a fitted line,
where w is in this Math expression:

y = Xw

And y and X are observations from a scatter plot.

Demo:
python class03p13.py
"""

import pandas as pd
import numpy  as np

csvfile_s  = 'http://spy611.com/csv/allpredictions.csv'
cp_df      = pd.read_csv(csvfile_s).sort_values(['cdate'])
cp2016_sr  = (cp_df.cdate > '2016') & (cp_df.cdate < '2017')
cp2016_df  = cp_df[['cdate','cp']][cp2016_sr]
daycount_i = cp2016_df.index.size

def colvec(arylst):
    # This should help me create column vectors from arrays or lists:
    rowcount_i = len(arylst)
    return np.array(arylst).reshape((rowcount_i,1))

# Study this image:
# http://ml4.herokuapp.com/class03/wsoln.png
# Y is easy to get, I should get Y first.
# I should transform the prices into a column vector of y-values:
yvals_a = colvec(cp2016_df.cp)

# Next I should work with X.

# I simplify; X-values are simple integers starting at 0:
x_a = colvec(range(daycount_i))
# Notice that I reshaped it into a column.
# I should pre-pend a column vector of ones:

ones_l = [1]*daycount_i
ones_a = colvec(ones_l)

# I should build xvals_a from column of ones then integers:
xvals_a = np.hstack((ones_a,x_a))

# Now, I have X and Y, I should implement Linear Algebra with NumPy:
lhs_a = np.linalg.pinv(np.matmul(xvals_a.T,xvals_a))
rhs_a = np.matmul(xvals_a.T,yvals_a)
w_a   = np.matmul(lhs_a,rhs_a)

print('w for a line fitted to the GSPC prices is this:')
print(w_a)

'bye'
