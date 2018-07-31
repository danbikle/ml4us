"""
demo2.py

This script should demonstrate calculation of R-Squared AKA R2.

demo:
~/anaconda3/bin/python -i demo2.py
"""

import pandas as pd
import numpy  as np
import sklearn
from sklearn import linear_model

# I should create a Data Frame with three observations.
# y of last observation deviates by 1%:
obs_df = pd.DataFrame({'x1':[10,20,30],'x2':[10,20,30], 'y':[100,200,303]})
# I should now have this DataFrame:
'''
>>> obs_df
   x1  x2    y
0  10  10  100
1  20  20  200
2  30  30  303
'''

x_a = np.array(obs_df[['x1','x2']])
# I should now have this Numpy Array:
'''
>>> x_a
array([[10, 10],
       [20, 20],
       [30, 30]])
'''

y_a = obs_df.y
# I should now have this Numpy Array:
'''
>>> y_a
0    100
1    200
2    303
Name: y, dtype: int64
'''

# I should create a LinearRegression model from the data:
linr_mod = linear_model.LinearRegression()
linr_mod.fit(x_a, y_a)
# I should see coefficents:
linr_mod.intercept_ # I call this w0 coefficent (s.b. near 0.0)
linr_mod.coef_      # w1, w2 (s.b. near 5.0)

# I should use the model to get three predictions:
yhat_a = linr_mod.predict(x_a)
# I should now have this Numpy Array:
'''
>>> yhat_a
array([  99.5,  201. ,  302.5])
'''

# I should use sklearn to calculate R-Squared:
# http://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html
r2sklearn_f = sklearn.metrics.r2_score(y_a, yhat_a)
# I should see:
'''
>>> r2sklearn_f
0.999927205668
'''

# I should use ISLR ch3 formula to calculate R-Squared:
# http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Seventh%20Printing.pdf
rss_f  = np.sum((y_a - yhat_a)**2)
tss_f  = np.sum((y_a - np.mean(y_a))**2)
myr2_f = 1 - rss_f/tss_f
# I should see:
'''
>>> myr2_f
0.999927205668252
'''
# myr2_f should be near r2sklearn_f

print('obs_df:')
print(obs_df)
print('r2sklearn_f:')
print(r2sklearn_f)
print('myr2_f:')
print(myr2_f)

'bye'
