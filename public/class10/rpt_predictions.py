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

'bye'

