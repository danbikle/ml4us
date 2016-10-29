# hr_model.r

# This script should use a function and a loop to create many models.
# This script depends on genf.r to run first to create feat.csv

# Ref:
# http://www.ml4.us/cclasses/class07#hr

# Demo:
# R -f hr_model.r

create_model = function(yr_i, size_i) {
  # I should load features from CSV:
  feat_df = read.csv('feat.csv')

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
  
  # I should get strings like this: '01_2' which corresponds to January_Tuesday.
  train_df$moydow = format(as.Date(train_df$cdate),"%m_%w")
  
  # I should get rows where pctlag1 < 0:
  down_v = (train_df$pctlag1 < 0)
  # I should get rows where pctlag1 >= 0:
  up_v   = (train_df$pctlag1 >=0)
  
  # I should use aggregate() to sum(pctlead) groupby Month-of-Year, Day-of-Week:
  mdown_df = aggregate(pctlead ~ moydow, train_df[down_v,], sum)
  mup_df   = aggregate(pctlead ~ moydow, train_df[up_v,]  , sum)
  # I should hstack them so I can use features to look up pctlead:
  pctlead_after_down_pctlag = round(mdown_df$pctlead,2)
  pctlead_after_up_pctlag   = round(mup_df$pctlead  ,2)
  moydow                    = mup_df$moydow
  model1_df = data.frame(moydow, pctlead_after_down_pctlag, pctlead_after_up_pctlag)
  
  # The model is ready for use.
  # I should write it to CSV so a predictor function can ask for predictions later:
  csv_s = paste('model',yr_i,'.csv',sep='')
  write.csv(model1_df,csv_s, row.names=FALSE)

  # The model should be written as a csv now.
  # The csv should look like: 'model2015.csv'
  return(csv_s)
}

# I should use a loop to create many models:
model_size_i = 25 # years
for (yr_i in c(2000:2016))
{
  fn_s = create_model(yr_i,model_size_i)
  print(fn_s)
}

'bye'
