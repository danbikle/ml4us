# hm13.r

# This script should generate a heatmap from GSPC dates and prices.
# Ref:
# http://www.tsds4.us/cclasses/class07bk20

# Demo:
# R -f hm13.r

# # I should get GSPC dates and prices:
# gspc0_df = read.csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
# 
# # I should identify each row by Date instead of an integer:
# # row.names(gspc0_df) = gspc0_df$Date
# 
# # I should order by Date:
# gspc1_df = gspc0_df[order(gspc0_df$Date),]
# 
# head(gspc1_df)
# 
# # I should write the df to a csv:
# write.csv(gspc1_df,'gspc1_df.csv', row.names=FALSE)

gspc2_df = read.csv('gspc1_df.csv')

gspc3_df = data.frame(gspc2_df$Date,gspc2_df$Close)

colnames(gspc3_df) = c('cdate','cp')

# I should compute pctlead,pctlag1 from cp
len_i            = length(gspc3_df$cp)
last_f           = gspc3_df$cp[len_i]
leadp_v          = c(gspc3_df$cp, last_f)[1:len_i+1]
gspc3_df$pctlead = 100 * (leadp_v - gspc3_df$cp) / gspc3_df$cp
gspc3_df$pctlag1 = c(0, gspc3_df$pctlead)[1:len_i]

# I should get Month-of-Year, Day-of-Week from cdate.
# I should get a column like this: 01_2 which corresponds to January_Tuesday.
gspc3_df$moydow = format(as.Date(gspc3_df$cdate),"%m_%w")
tail(gspc3_df)

# I should get rows after 1990-01-01:
pred_v   = (as.Date(gspc3_df$cdate) > '1990-01-01')
gspc4_df = gspc3_df[ pred_v , ]

# I should use aggregate() to sum(pctlead) groupby Month-of-Year, Day-of-Week:
moydow0_df = aggregate(pctlead ~ moydow, gspc4_df, sum)
head(moydow0_df)

bbyyee
# I should use better colnames:
colnames(moydow0_df) = c('moydow','sum_pctlead')


# Above DF is long and skinny.
# The days are vertically stacked.
'bye'
