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
write.csv(gspc1_df,'gspc1.csv', row.names=FALSE)

gspc2_df = read.csv('gspc1.csv')

gspc3_df = data.frame(gspc2_df$Date,gspc2_df$Close)

colnames(gspc3_df) = c('cdate','cp')

# I should compute pctlead,pctlag1 from cp
len_i            = length(gspc3_df$cp)
last_f           = gspc3_df$cp[len_i]
leadp_v          = c(gspc3_df$cp, last_f)[1:len_i+1]
gspc3_df$pctlead = 100 * (leadp_v - gspc3_df$cp) / gspc3_df$cp
gspc3_df$pctlag1 = c(0, gspc3_df$pctlead)[1:len_i]

# I should pick the test year which then helps me constrain the training years.
yr_test_i    = 2016
train_size_i = 25 # years

# I should use yr_test_i and train_size_i to get yr_train_end_i yr_train_start_i
yr_train_end_i   = 2015
yr_train_start_i = yr_test_i - train_size_i

# I should constrain the training data.
yr_v     = strtoi(format(as.Date(gspc3_df$cdate),"%Y" ))
pred1_v  = (yr_v >= yr_train_start_i)
pred2_v  = (yr_v <= yr_train_end_i)
pred3_v  = (pred1_v & pred2_v)
train_df = gspc3_df[ pred3_v , ]

head(train_df)
tail(train_df)

# I should build a model from train_df.

# I should get strings like this: '01_2' which corresponds to January_Tuesday.
train_df$moydow = format(as.Date(train_df$cdate),"%m_%w")

#row.names(train_df) = train_df$moydow

# I should get rows where pctlag1 < 0:
down_v = (train_df$pctlag1 < 0)
# I should get rows where pctlag1 >= 0:
up_v   = (train_df$pctlag1 >=0)

# I should use aggregate() to sum(pctlead) groupby Month-of-Year, Day-of-Week:
mdown_df = aggregate(pctlead ~ moydow, train_df[down_v,], sum)
mup_df   = aggregate(pctlead ~ moydow, train_df[up_v,]  , sum)
# I should hstack them:
pctlead_after_down_pctlag = mdown_df$pctlead
pctlead_after_up_pctlag   = mup_df$pctlead
model1_df = data.frame(pctlead_after_down_pctlag, pctlead_after_up_pctlag)
row.names(model1_df) = mup_df$moydow

head(model1_df)
tail(model1_df)
