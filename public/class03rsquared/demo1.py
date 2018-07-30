"""
demo1.py

This script should demonstrate calculation of R-Squared AKA R2.

demo:
~/anaconda3/bin/python demo1.py
"""

import pandas as pd
import numpy  as np
from sklearn import linear_model

# I should create a Data Frame with three observations:
obs_df = pd.DataFrame({'x1':[10,20,30],'x2':[10,20,30], 'y':[100,200,300]})

# I should now have this DataFrame:
'''
>>> obs_df
   x1  x2    y
0  10  10  100
1  20  20  200
2  30  30  300
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
2    300
Name: y, dtype: int64
'''

# I should create a LinearRegression model from the data:
linr_mod = linear_model.LinearRegression()
linr_mod.fit(x_a,y_a)
# I should see coefficents:
linr_mod.intercept_ # I call this w0 coefficent (s.b. near 0.0)
linr_mod.coef_      # w1, w2 (s.b. near 5.0)

# I should use the model to get three predictions:
pred_a = linr_mod.predict(x_a)
# I should now have this Numpy Array:
'''
>>> pred_a
array([ 100.,  200.,  300.])
'''

'bye'
