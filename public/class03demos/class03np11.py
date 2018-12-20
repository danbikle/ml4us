"""
class03np11.py

This script should create a NumPy Array From Pandas DataFrame of GSPC prices.

Demo:
python class03np11.py
"""

import pandas as pd
import numpy  as np

prices_df = pd.read_csv('https://tkrprice.herokuapp.com/static/gspc.csv')
prices_a  = np.array(prices_df)

# I should print the first 9 rows to help me see the NumPy Array:
print(prices_a[:9])

'bye'
