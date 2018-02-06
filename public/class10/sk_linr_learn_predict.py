"""
sk_linr_learn_predict.py

This script should learn from features in feat.csv and calculate predictions.

Demo:
python sk_linr_learn_predict.py
"""

import os
import pdb
import pandas as pd
import numpy  as np
from sklearn import linear_model

# I should prep for a new csv file
fn_s = 'sk_linr_predictions.csv'
os.system('rm -f '+fn_s)

feat_df = pd.read_csv('feat.csv')
train_i = 20 # amount of training years
# I should loop through some years I want to predict:
lastyr2predict_i = 2017
for yr_i in range(2010,lastyr2predict_i+1):
    yr_begin_i    = yr_i - train_i
    trainstart_sr = feat_df.cdate > str(yr_begin_i)
    trainend_sr   = feat_df.cdate < str(yr_i)
    train_sr   = trainstart_sr & trainend_sr
    train_df   = feat_df[train_sr]
    test_sr    = feat_df.cdate.str.match(str(yr_i))
    test_df    = feat_df[test_sr]
    train_a    = np.array(train_df)[:,[2,4,5,6]]
    test_a     = np.array(test_df)[ :,[2,4,5,6]]
    x_a        = train_a[:,1:]
    y_a        = train_a[:,0].reshape((-1,1))
    linr_model = linear_model.LinearRegression()
    linr_model.fit(x_a,y_a)
    xtest_a        = test_a[:,1:]
    predictions_a  = linr_model.predict(xtest_a)
    predictions_df = test_df[['cdate','closep','pctlead']].copy()
    predictions_df['prediction']    = predictions_a[:,0].tolist()
    predictions_df['effectiveness'] = np.sign(predictions_df.prediction)*predictions_df.pctlead
    # if file exists I should append else write (with header)
    if os.path.isfile(fn_s):
        with open(fn_s, 'a') as fh:
            predictions_df.to_csv(fh, float_format='%4.4f', index=False, header=False)
    else:
        predictions_df.to_csv(fn_s, float_format='%4.4f', index=False)

'bye'
