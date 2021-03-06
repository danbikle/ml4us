"""
class03np45.py

This script should slice and dice

Demo:
python class03np45.py
"""

import pandas as pd
import numpy  as np

prices_df = pd.read_csv('https://ml4.herokuapp.com/csv/GSPC.csv')

# I should do it the numpy way:
prices_a = np.array(prices_df)
s1_a = prices_a[5:11,[0,4]]
print(s1_a)
# Numpy is more constrained.
# I should specify rows first, columns second.

'bye'
