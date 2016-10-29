# get_predictions.r

# This script should use a function and a loop to get many predictions.
# This script depends on genf.r to create feat.csv
# This script depends on hr_model.r to run first to create modelYYYY.csv

# Ref:
# http://www.ml4.us/cclasses/class07#hr

# Demo:
# R -f get_predictions

get_prediction = function(dt){
  return(1.1)
}

feat_df = read.csv('feat.csv')

tail(feat_df$cdate)

'bye'
