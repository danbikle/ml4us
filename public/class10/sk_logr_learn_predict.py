"""
sk_logr_learn_predict.py

This script should learn from features in feat.csv and calculate predictions.

Demo:
python sk_logr_learn_predict.py
"""

import os
import pdb
import pandas as pd
import numpy  as np
from sklearn import linear_model

# I should prep for a new csv file
fn_s = 'sk_logr_predictions.csv'
os.system('rm -f '+fn_s)

feat_df = pd.read_csv('feat.csv')
# I should visualize some feature navigators:
# cdate,closep,pctlead,updown       3
#,pctlag1,pctlag2,pctlag3,pctlag4   7
#,pctlag5,pctlag6,pctlag7,pctlag8  11
# ,pctlag12,pctlag16,slope2,slope3 15
# ,slope4,slope5,slope6,slope7     19
# ,slope8,slope9,dow,moy           23
# I dont want all the above columns:
col_iwant_l = [3,4,6,11,15,19,22,23]
# which are these:
# pctlead
# pctlag1
# pctlag3
# pctlag8
# slope3
# dow
# moy

train_i = 25 # amount of training years
# I should loop through some years I want to predict:
lastyr2predict_i = 2017
for yr_i in range(2010,lastyr2predict_i+1):
    yr_begin_i    = yr_i - train_i
    trainstart_sr = feat_df.cdate > str(yr_begin_i)
    trainend_sr   = feat_df.cdate < str(yr_i)
    train_sr   = trainstart_sr & trainend_sr
    train_df   = feat_df.loc[train_sr]
    test_sr    = feat_df.cdate.str.match(str(yr_i))
    test_df    = feat_df.loc[test_sr]
    train_a    = np.array(train_df.iloc[:,col_iwant_l])
    test_a     = np.array(test_df.iloc[ :,col_iwant_l])
    x_a        = train_a[:,1:]
    y_a        = train_a[:,0]
    logr_model = linear_model.LogisticRegression()
    logr_model.fit(x_a,y_a)
    xtest_a        = test_a[:,1:]
    predictions_a  = logr_model.predict_proba(xtest_a)
    predictions_df = test_df[['cdate','closep','pctlead']].copy()
    predictions_df['prediction']    = predictions_a[:,1].tolist()
    predictions_df['effectiveness'] = np.sign(predictions_df.prediction-0.5)*predictions_df.pctlead
    # if file exists I should append else write (with header)
    if os.path.isfile(fn_s):
        with open(fn_s, 'a') as fh:
            predictions_df.to_csv(fh, float_format='%4.4f', index=False, header=False)
    else:
        predictions_df.to_csv(fn_s, float_format='%4.4f', index=False)

'bye'
