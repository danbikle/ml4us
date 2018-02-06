"""
rpt_predictions.py

This script should report effectiveness of predictions.

Demo:
python rpt_predictions.py sk_linr_predictions.csv
"""

import os
import pdb
import sys
import pandas as pd
import numpy  as np

if len(sys.argv) > 1:
    fn_s = sys.argv[1] #'sk_linr_predictions.csv'
else:
    fn_s = 'sk_linr_predictions.csv'

predictions_df = pd.read_csv(fn_s)
longonly_eff   = np.sum(predictions_df.pctlead)
model_eff      = np.sum(predictions_df.effectiveness)

print('Reporting on predictions in this file:')
print(fn_s)
print('model_eff:')
print(model_eff)
print('longonly_eff:')
print(longonly_eff)
print('model_eff/longonly_eff:')
print(model_eff/longonly_eff)

# I should create a plot:
plot0_df          = predictions_df.iloc[:-1][['cdate','closep']]
plot0_df['cdate'] = pd.to_datetime(plot0_df['cdate'], format='%Y-%m-%d')
plot0_df.head()
plot0_df.columns = ['cdate','Long_Only']

# I should create effectiveness-line for predictions.
# I have two simple rules:
# 1. If blue line moves $x, then model-line moves $x.
# 2. If model is True, model-line goes up.

len_i   = len(plot0_df)
cp_sr   = plot0_df.Long_Only
model_l = [cp_sr.iloc[0]]

for row_i in range(len_i-1):
    cp     = cp_sr.iloc[row_i]
    cpnext = cp_sr.iloc[row_i+1]
    cpdelt = np.abs(cpnext - cp)
    modeldelt = np.sign(predictions_df.effectiveness.iloc[row_i])*cpdelt
    model_l.append(model_l[row_i]+modeldelt)

plot0_df['Model'] = model_l

import matplotlib
matplotlib.use('Agg')
# Order is important here.
# Do not move the next import:
import matplotlib.pyplot as plt

plot1_df = plot0_df.set_index(['cdate'])
plot1_df.plot.line(title="Model Effectiveness Visualization", figsize=(11,7))
plt.savefig(fn_s+'.png')
plt.close()

'bye'

