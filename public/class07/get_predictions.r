# get_predictions.r

# This script should use a function and a loop to get many predictions.
# This script depends on genf.r to create feat.csv
# This script depends on hr_model.r to run first to create modelYYYY.csv

# Ref:
# http://www.ml4.us/cclasses/class07#hr

# Demo:
# R -f get_predictions.r

get_prediction = function(dt_s){
  return(1.1)
}

feat_df = read.csv('feat.csv')

dates_v = tail(feat_df$cdate)

for (dt_s in dates_v){
  # I should get value of YYYY so I can locate modelYYYY.csv
  yr_s  = format(as.Date(dt_s),"%Y")
  csv_s = paste('model',yr_s,'.csv', sep='')
  # I should get value of pctlag, moydow from feat_df using dt_s.
  row_v    = (feat_df$cdate == dt_s)
  pctlag_f = feat_df[row_v,]$pctlag
  moydow_s = feat_df[row_v,]$moydow
  print(feat_df[row_v,])
  # I should use pctlag_f to pick which column in the model csv I want:
  col_i = 2
  if (pctlag_f > 0){
    col_i = 3
  }
  # I should use moydow to get a row from model:
  model_df = read.csv(csv_s)
  pred_v = (moydow_s == model_df$moydow)
  print(model_df[pred_v ,])
  print(model_df[pred_v , col_i])
  stophere
}

'bye'
