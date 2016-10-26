# hr10.r

# This script should build a heuristic pctlead-model from pctlag1, and date-features

# Ref:
# http://www.ml4.us/cclasses/class07#hr

# Demo:
# R -f hr10.r

# I should get GSPC dates and prices:
gspc0_df = read.csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')

# I should identify each row by Date instead of an integer:
# row.names(gspc0_df) = gspc0_df$Date

# I should order by Date:
gspc1_df = gspc0_df[order(gspc0_df$Date),]

head(gspc1_df)
tail(gspc1_df)

# I should write the df to a csv:
write.csv(gspc1_df,'gspc1_df.csv', row.names=FALSE)

gspc2_df = read.csv('gspc1_df.csv')

gspc3_df = data.frame(gspc2_df$Date,gspc2_df$Close)

colnames(gspc3_df) = c('cdate','cp')

# I should compute pctlead,pctlag1 from cp
len_i            = length(gspc3_df$cp)
last_f           = gspc3_df$cp[len_i]
leadp_v          = c(gspc3_df$cp, last_f)[1:len_i+1]
gspc3_df$pctlead = 100 * (leadp_v - gspc3_df$cp) / gspc3_df$cp
gspc3_df$pctlag1 = c(0, gspc3_df$pctlead)[1:len_i]

# I should get Day-of-Week, Month-of-Year from cdate:
moy_v = format(as.Date(gspc3_df$cdate),"%-m")
dow_v = format(as.Date(gspc3_df$cdate),"%w" )

# I should concatenate moy_v, dow_v.
# I should get strings like this: '01_2' which corresponds to January_Tuesday.
moydow_v = format(as.Date(gspc3_df$cdate),"%m_%w")

# I should pick the test year which then helps me constrain the training years.
yr_test_i    = 2016
train_size_i = 25 # years

# I should use yr_test_i and train_size_i to get yr_train_end_i yr_train_start_i
yr_train_end_i = 2015
yr_train_start_i = yr_test_i - train_size_i
