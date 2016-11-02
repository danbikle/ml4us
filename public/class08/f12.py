# f12.py

# This script should generate features from csv data.

import pandas as pd

f10_df = pd.read_csv('fx3/eur.csv', names=['ts','cp'])

slopes_a = [2,3,4,5,6,7,8,9]

# I should compute piplead:
f10_df['piplead'] = (10000.0*(f10_df.cp.shift(-1) - f10_df.cp) / f10_df.cp).fillna(0)
print(f10_df.head())


'bye'
