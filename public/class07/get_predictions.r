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
  print(dt_s)
  # I should get value of YYYY so I can locate modelYYYY.csv
  # I should get value of pctlag from feat_df using dt_s.
  yr_s  = format(as.Date(dt_s),"%Y")
  csv_s = paste('model',yr_s,'.csv', sep='')
  print(csv_s)
  stophere
}

'bye'
