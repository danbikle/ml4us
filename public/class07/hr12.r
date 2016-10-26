# hr12.r

# This script should use a function and a loop to create many models.

# Ref:
# http://www.ml4.us/cclasses/class07#hr

# Demo:
# R -f hr12.r

# I should try to generate a model from these inputs:
my_yr_i      = 2015
model_size_i = 25 # years

create_model = function(yr_i, size_i) {


  # The model should be written as a csv now.
  # The csv should look like: 'model2015.csv'
  return(TRUE)
}

# I should get prices:

# I should get GSPC dates and prices:
gspc0_df = read.csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
# I should order by Date:
gspc1_df = gspc0_df[order(gspc0_df$Date),]
# I should only use Date and Closing Price:
gspc3_df = data.frame(gspc1_df$Date,gspc1_df$Close)
colnames(gspc3_df) = c('cdate','cp')
write.csv(gspc3_df,'gspc3.csv', row.names=FALSE)
tail(gspc3_df)

create_model(my_yr_i,model_size_i)


