"""
rpt_predictions.py

This script should report effectiveness of predictions.

Demo:
python rpt_predictions.py
"""

import os
import pdb
import pandas as pd
import numpy  as np

fn_s = 'sk_linr_predictions.csv'
predictions_df = pd.read_csv(fn_s)
predictions_df.tail()

longonly_eff = np.sum(predictions_df.pctlead)
model_eff    = np.sum(predictions_df.effectiveness)

print('model_eff:')
print(model_eff)
print('longonly_eff:')
print(longonly_eff)
print('model_eff/longonly_eff:')
print(model_eff/longonly_eff)

'bye'

