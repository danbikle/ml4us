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

# I should generate labels from pctlead:

train_df$labels = (train_df$pctlead > median(train_df$pctlead))


# Now I should learn:
mymodel = glm(labels ~ pctlag1 + moy + dow, data=train_df, family='binomial')

# The above model assumes that each label relies somewhat on pctlag1,moy, and dow
# The model returns the probability that label is TRUE
# If the probability is above 0.51 I consider that a bullish prediction.
# If the probability is below 0.49 I consider that a bearish prediction.

# I should load test data
yr_test     = yr_i
yr_test_v   = strtoi(format(as.Date(feat_df$cdate),"%Y"))
pred_test_v = (yr_test_v == yr_test)
test_df     = feat_df[pred_test_v , ]
tail(test_df)

predictions_v = predict(mymodel,test_df, type='response')
test_df$prediction = predictions_v
test_df$eff = (0.5 - test_df$prediction) * test_df$pctlead
tail(test_df)

# I should write predictions to CSV
csv_s = paste('predictions',yr_test,'.csv',sep='')
write.csv(test_df,csv_s, row.names=FALSE)

'bye'
