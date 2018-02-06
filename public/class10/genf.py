"""
genf.py

This script should generate feat.csv from GSPC.csv

The file, feat.csv, is full of machine learning features.

We have two types of features:
  - price features
  - date features

Demo:
~/anaconda3/bin/python genf.py
"""

import pdb
import pandas as pd
import numpy  as np

# I should get prices 
prices0_df = pd.read_csv('GSPC.csv')

prices1_df = prices0_df[['Date','Close']].sort_values(['Date'])
prices1_df.columns = ['Date','Price']


    
