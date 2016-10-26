# hr11.r

# This script should demo how to create a function which gets a prediction.

# Ref:
# http://www.ml4.us/cclasses/class07#hr

# Demo:
# R -f hr11.r


# I should try to get a prediction.

my_yr_test_i    = 2016
my_month_s      = '10'
my_day_ofweek_i = 3
my_pctlag_f     = -0.17

get_prediction = function(yr_test_i, month_s, day_ofweek_i, pctlag_f){
  # I should transform the inputs:
  csv_s      = paste('model',yr_test_i,'.csv',sep='' )
  moydow_s   = paste(month_s,day_ofweek_i    ,sep='_')
  # I should get the model
  my_model_l = read.csv(csv_s)
  # I should get a row from model
  pred_v     = (my_model_l$moydow == moydow_s)
  if (my_pctlag_f < 0) {
    # I should get a cell from row
    prediction_f = my_model_l[pred_v,2]
    } else {
    prediction_f = my_model_l[pred_v,3]
  }
  return(prediction_f)
}

prediction_f = get_prediction(my_yr_test_i, my_month_s, my_day_ofweek_i, my_pctlag_f)
prediction_f

