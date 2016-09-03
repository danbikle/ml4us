# class03p15.py

# This script should use Linear Algebra to find RMSE of a fitted line.
# ref:
# http://www.ml4.us/class03/pdf1.png
# http://www.stat.purdue.edu/~jennings/stat514/stat512notes/topic3.pdf

import pandas as pd
import numpy  as np
import pdb
csvfile   = 'http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC'
cp_df     = pd.read_csv(csvfile).sort_values(['Date'])
cp2016_sr = (cp_df.Date > '2016') & (cp_df.Date < '2017')
cp2016_df = cp_df[['Date','Close']][cp2016_sr]

def colvec(arylst):
    # This should help me create column vectors from arrays or lists:
    return np.array(arylst).reshape((len(arylst),1))

x_a      = colvec(range(len(cp2016_df)))
ones_l   = [1]*len(cp2016_df)
ones_a   = colvec(ones_l)
xvals_a  = np.hstack((ones_a,x_a))
yvals_a  = colvec(cp2016_df.Close)
middle_a = np.linalg.pinv(np.matmul(xvals_a.T,xvals_a))
rhs_a    = np.matmul(xvals_a.T,yvals_a)
beta_a   = np.matmul(middle_a,rhs_a)

x_in_a   = xvals_a

yhat_a   = np.matmul(x_in_a,beta_a)

cp2016_df['yhat'] = yhat_a

sqdiffe = (cp2016_df.Close - cp2016_df.yhat)**2
print('RMSE between fitted line and closing price:')
rmse_f = np.sqrt(np.mean(sqdiffe))
print(rmse_f)

'bye'
