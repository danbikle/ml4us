"""
~/ml4/public/class04/logr10/logr12o.py.py

This script should implement the same ML idea as logr12o.py.scala:

- Read ml4.us/csv/GSPC.csv into DataFrame
- Generate dependent variable: "pctlead"
- Collect independent variables: slp2, ... slp9
- Create train_df from a filter: 1986-01-01 until 2016-01-01
- Create test_df  from a filter: 2016-01-01 until 2017-01-01
- Calculate value of class_boundry_f from train_df.pctlead.mean()
- Transform class_boundry_f into labels
- Create train_a from train_df
- Use LogisticRegression to fit model to train_a
- Predict observations in test_a
- Report accuracy and effectiveness of predictions

Demo:
python logr12o.py.py
"""

import pandas as pd
import numpy  as np
import pdb
from sklearn import linear_model

# I should Read ml4.us/csv/GSPC.csv into DataFrame
gspc_df = pd.read_csv('https://ml4.herokuapp.com/csv/GSPC.csv')

# I should Generate dependent variable: "pctlead"
leadp_sr   = gspc_df.Close.shift(-1)
pctlead_sr = (100.0*(leadp_sr - gspc_df.Close)/gspc_df.Close).fillna(0)
gspc_df['pctlead'] = pctlead_sr
  
# I should Collect independent variables: slp2, ... slp9
for slope_i in [2,3,4,5,6,7,8,9]:
  rollx          = gspc_df.rolling(window=slope_i)
  col_s          = 'slp'+str(slope_i)
  slope_sr       = 100.0 * (rollx.mean().Close - rollx.mean().Close.shift(1))/rollx.mean().Close
  gspc_df[col_s] = slope_sr

# I should Create train_df, train_a from a filter: 1986-01-01 until 2016-01-01
filter_train_sr = (gspc_df.Date > '1986') & (gspc_df.Date < '2016')
columns_iwant_l = ['Date','pctlead','slp2','slp3','slp4','slp5','slp6','slp7','slp8','slp9']
train_df        = gspc_df[columns_iwant_l].loc[filter_train_sr]

# I should Create test_df,  test_a  from a filter: 2016-01-01 until 2017-01-01
filter_test_sr = (gspc_df.Date > '2016') & (gspc_df.Date < '2017')
test_df        = gspc_df[columns_iwant_l].loc[filter_test_sr]

# I should Calculate value of class_boundry_f from train_df.pctlead.mean()
pdb.set_trace()
class_boundry_f = train_df.pctlead.mean()
# I should Transform class_boundry_f into labels
labels_sr = train_df.pctlead > class_boundry_f

# I should Create train_a from train_df
train_a         = np.array(train_df)

# I should Use LogisticRegression to fit model to train_a
linr_model = linear_model.LogisticRegression()
x_a = train_a[:,2:] # I should get all rows and columns after columns: 0,1
y_a = np.array(labels_sr)
linr_model.fit(x_a, y_a)

# I should Predict observations in test_a
x_test_a      = test_a[:,2:]
predictions_a = linr_model.predict(x_test_a)

# I should Report accuracy and effectiveness of predictions
rpt_df               = test_df[['Date','pctlead']].copy()
rpt_df['prediction'] = predictions_a[:,0].tolist()

'bye'
