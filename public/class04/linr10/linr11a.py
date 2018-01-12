"""
~/ml4/public/class04/linr10/linr11a.py

This script should implement the same ML idea as linr11a.scala:

- Read ml4.us/csv/GSPC.csv into DataFrame
- Generate dependent variable: "pctlead"
- Collect independent variables: slp2, ... slp9
- Create train_df, train_a from a filter: 1986-01-01 until 2016-01-01
- Create test_df,  test_a  from a filter: 2016-01-01 until 2017-01-01
- Use LinearRegression to fit model to train_a
- Predict observations in test_a
- Report accuracy and effectiveness of predictions

Demo:
python linr11a.py
"""
