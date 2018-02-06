"""
sk_linr_learn_predict.py

This script should learn from features in feat.csv and calculate predictions.

Demo:
python sk_linr_learn_predict.py
"""

import pdb
import pandas as pd
import numpy  as np

feat_df = pd.read_csv('feat.csv')
train_i = 20 # amount of training years
# I should loop through some years I want to predict:
lastyr2predict_i = 2017
for yr_i in range(2016,lastyr2predict_i+1):
    yr_begin_i    = yr_i - train_i
    trainstart_sr = feat_df.cdate > str(yr_begin_i)
    trainend_sr   = feat_df.cdate < str(yr_i)
    train_sr      = trainstart_sr & trainend_sr
    train_df      = feat_df[train_sr]
    test_sr       = feat_df.cdate.str.match(str(yr_i))
    test_df       = feat_df[test_sr]
    print(test_df.head(2))

'bye'
