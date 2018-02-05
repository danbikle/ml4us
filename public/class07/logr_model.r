# logr_model.r

# This script should create a logistic regression model.

# Ref:
# http://www.ml4.us/cclasses/class07#hr

# Demo:
# R -f logr_model.r

train_test_logr = function(feat_df,yr_i,size_i){
  # This function should train and then test using Logistic Regression and data in feat_df.
  
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
  # So, I should generate labels from pctlead:
  train_df$labels = (train_df$pctlead > median(train_df$pctlead))
  
  # Now I should learn:
  mymodel = glm(labels ~ pctlag1 + moy + dow, data=train_df, family='binomial')
  
  # The above model assumes that each label relies somewhat on pctlag1,moy, and dow
  # The model returns the probability that label is TRUE
  # If the probability is above 0.51 I consider that a bullish prediction.
  # If the probability is below 0.49 I consider that a bearish prediction.
  
  # I should load test data
  yr_test            = yr_i
  yr_test_v          = strtoi(format(as.Date(feat_df$cdate),"%Y"))
  pred_test_v        = (yr_test_v == yr_test)
  test_df            = feat_df[pred_test_v , ]
  test_df$prediction = predict(mymodel,test_df, type='response') 
  test_df$eff        = sign(test_df$prediction-0.5) * test_df$pctlead
  test_df$accurate   = (test_df$eff >= 0)
  # I should write predictions to CSV
  csv_s = paste('predictions',yr_test,'.csv',sep='')
  write.csv(test_df,csv_s, row.names=FALSE)
  return(csv_s)
} # train_test_logr = function(feat_df,yr_i,size_i)

# I should load features from CSV:
feat_df = read.csv('feat.csv')
size_i  = 25

for (yr_i in c(2000:2018)){
  pf_s = train_test_logr(feat_df,yr_i,size_i)
  print(pf_s)
}

# I should report effectiveness, accuracy:
sum_eff_long_f      = 0
sum_eff_logr_f      = 0
sum_long_accuracy_i = 0
sum_accuracy_i      = 0
sum_all_i           = 0
for (yr_i in c(2000:2018)){
  csv_s = paste('predictions',yr_i,'.csv',sep='')
  p_df = read.csv(csv_s)
  sum_eff_long_f      = sum_eff_long_f + sum(p_df$pctlead)
  sum_eff_logr_f      = sum_eff_logr_f + sum(p_df$eff)
  sum_long_accuracy_i = sum_long_accuracy_i + sum((p_df$pctlead > 0))
  sum_accuracy_i      = sum_accuracy_i + sum(p_df$accurate)
  sum_all_i           = sum_all_i      + length(p_df$accurate)
}

print('Long-Only Effectiveness:')
print(sum_eff_long_f)

print('Logistic-Regression Effectiveness:')
print(sum_eff_logr_f)

print('Long-Only Accuracy:')
acc_long_f = 100.0 * sum_long_accuracy_i / sum_all_i
print(acc_long_f)

print('Logistic-Regression Accuracy:')
acc_logr_f = 100.0 * sum_accuracy_i / sum_all_i
print(acc_logr_f)

'bye'
