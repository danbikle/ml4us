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
    yr_begin_i   = yr_i - train_i
    predstart_sr = feat_df.cdate > str(yr_begin_i)
    predend_sr   = feat_df.cdate < str(yr_i)
    pred_sr      = predstart_sr & predend_sr
    train_df     = feat_df[pred_sr]
    print(train_df.tail(2))

'bye'
