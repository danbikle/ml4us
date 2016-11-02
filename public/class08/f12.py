# f12.py

# This script should generate features from csv data.

import pandas as pd

f10_df = pd.read_csv('fx3/eur.csv', names=['ts','cp'])
print(f10_df.tail())


'bye'
