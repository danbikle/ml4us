"""
How to calculate "Inverse of X"?

Calculating the Inverse of X is not always easy,
but NumPy offers a method called pinv() which gives us a good approximation.

Now, I can offer some NumPy syntax to fit a line to a scatter plot of three points:
"""
import numpy as np
import pandas as pd
x0 = 0.0;  y0 = 1.0
x1 = 1.0;  y1 = 1.5
x2 = 1.10; y2 = 1.48

# It is easy to build a NumPy array from rows.
# But,
# To build a NumPy array from columns,
# I first create a Pandas DF from columns,
# then convert the DF to array:

col0_l = [1, 1, 1]
col1_l = [x0, x1, x2]
my_df = pd.DataFrame({'col0': col0_l, 'col1': col1_l})
x_a   = np.array(my_df)
y_a   = np.array([y0, y1, y2]).reshape(3,1)

lhs_a = np.linalg.pinv(np.matmul(x_a.T, x_a))
rhs_a = np.matmul(x_a.T, y_a)
w_a   = np.matmul(lhs_a, rhs_a)
"""
After I ran the above syntax on my laptop, NumPy gave me this value for w_a:

>>> w_a
array([[1.00315315],
       [0.46216216]])
>>>
"""
