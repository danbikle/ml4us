# class03np11.py

# Create a NumPy Array From Pandas DataFrame of GSPC prices.

import pandas as pd
import numpy  as np

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_a  = np.array(prices_df)

# I should print the first 9 rows to help me see the NumPy Array:
print(prices_a[:9])

'bye'
