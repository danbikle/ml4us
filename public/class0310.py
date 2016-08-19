# class0310.py

# Use Pandas to plot prices of GSPC for 2016.

import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
from datetime import datetime

csvfile = 'http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC'
cp_df   = pd.read_csv(csvfile)
pdb.set_trace()
cp_df.head()
'bye'
