# hr12.r

# This script should use a function and a loop to create many models.

# Ref:
# http://www.ml4.us/cclasses/class07#hr

# Demo:
# R -f hr12.r

create_model = function(yr_i, size_i) {
  # I should load prices from CSV:
  gspc3_df = read.csv('gspc3.csv')
  # I should compute pctlead,pctlag1 from cp
  len_i            = length(gspc3_df$cp)
  last_f           = gspc3_df$cp[len_i]
  leadp_v          = c(gspc3_df$cp, last_f)[1:len_i+1]
  gspc3_df$pctlead = 100 * (leadp_v - gspc3_df$cp) / gspc3_df$cp
  gspc3_df$pctlag1 = c(0, gspc3_df$pctlead)[1:len_i]

  # I should use compute end, start:
  yr_train_end_i   = yr_i - 1
  yr_train_start_i = yr_i - size_i
  
  # I should constrain the training data.
  yr_v     = strtoi(format(as.Date(gspc3_df$cdate),"%Y" ))
  pred1_v  = (yr_v >= yr_train_start_i)
  pred2_v  = (yr_v <= yr_train_end_i)
  pred3_v  = (pred1_v & pred2_v)
  train_df = gspc3_df[ pred3_v , ]
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

get_prices = function(){
  # I should get GSPC dates and prices:
  gspc0_df = read.csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
  # I should order by Date:
  gspc1_df = gspc0_df[order(gspc0_df$Date),]
  # I should only use Date and Closing Price:
  gspc3_df = data.frame(gspc1_df$Date,gspc1_df$Close)
  colnames(gspc3_df) = c('cdate','cp')
  write.csv(gspc3_df,'gspc3.csv', row.names=FALSE)
  tail(gspc3_df)
  # I should now see a new CSV:
  # gspc3.csv
}


# I should try to generate a model from these inputs:
my_yr_i      = 2015
model_size_i = 25 # years

# get_prices()
create_model(my_yr_i,model_size_i)

# I should use a loop to create many models:

for (yr_i in c(2000:2016))
{
  fn_s = create_model(yr_i,model_size_i)
  print(fn_s)
}

'bye'


