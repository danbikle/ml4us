"""
class03np12.py

Create a NumPy Array From Pandas DataFrame of GSPC prices.
"""

import pandas as pd
import numpy  as np

prices_df = pd.read_csv('http://ml4.us/csv/GSPC.csv')
prices_a  = np.array(prices_df)

# Sort the array by date string:
sorted_prices_a = np.sort(prices_a, axis=0)

# I should visualize it:
print(sorted_prices_a[:9])

'bye'
