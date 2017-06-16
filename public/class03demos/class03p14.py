"""
class03p14.py

This script should calculate a prediction.

I should predict the price 70 days after the first price.

ref:
http://www.ml4.us/class03/pdf1.png
http://www.stat.purdue.edu/~jennings/stat514/stat512notes/topic3.pdf
"""

import numpy  as np

beta_l = [[1.93878278e+03], [1.24198003e+00]]

# The first column of X-matrix is always 1:
xval_l = [[1,70]]

yhat_f = np.matmul(xval_l,beta_l)

print('I predict the price 70 days after the first price to be:')
print(yhat_f)

print('Using scalars, I predict the price 70 days after the first price to be:')
m       = 1.24198003
x       = 70
b       = 1938.78278
yhat2_f = m*x + b
print(yhat2_f)

'bye'

