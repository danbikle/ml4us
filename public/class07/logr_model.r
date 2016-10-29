# logr_model.r

# This script should create a logistic regression model.

# Ref:
# http://www.ml4.us/cclasses/class07#hr

# Demo:
# R -f logr_model.r


  # I should load features from CSV:
  feat_df = read.csv('feat.csv')

tail(feat_df)

yr_i = 2016
size_i = 25

  # I should use yr_i to compute end, start:
  yr_train_end_i   = yr_i - 1
  yr_train_start_i = yr_i - size_i
  
  # I should constrain the training data.
  yr_v     = strtoi(format(as.Date(feat_df$cdate),"%Y"))
  pred1_v  = (yr_v >= yr_train_start_i)
  pred2_v  = (yr_v <= yr_train_end_i)
  pred3_v  = (pred1_v & pred2_v)
  train_df = feat_df[ pred3_v , ]
  # I should build a model from train_df.
  
tail(train_df)

'bye'
