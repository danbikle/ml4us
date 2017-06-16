"""
class03p10.py

This script should use Pandas to plot prices of GSPC for 2016.
"""

import pandas as pd
import matplotlib.pyplot as plt

csvfile = 'http://spy611.herokuapp.com/csv/allpredictions.csv'
# Goog: In pandas how to sort a dataframe?
cp_df = pd.read_csv(csvfile).sort_values(['cdate'])
# Goog: In pandas how to filter?
cp2016_sr = (cp_df.cdate > '2016') & (cp_df.cdate < '2017')
cp2016_df = cp_df[['cdate','cp']][cp2016_sr]

# I should plot
cpdate2016_df = cp2016_df.set_index(['cdate'])
# Goog: In Pandas what is an index?
# Goog: In Pandas what does set_index do?
cpdate2016_df.plot.line(title="GSPC 2016")
plt.show() # This line might be slow

'bye'
