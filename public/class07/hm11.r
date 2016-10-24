# hm11.r

# This script should generate a heatmap from GSPC dates and prices.
# Ref:
# http://www.tsds4.us/cclasses/class07bk20

# Demo:
# R -f hm11.r

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

head(gspc3_df)
tail(gspc3_df)

# I should compute pctlead,pctlag1 from cp
len_i            = length(gspc3_df$cp)
last_f           = gspc3_df$cp[len_i]
gspc3_df$leadp   = c(gspc3_df$cp, last_f)[1:len_i+1]
gspc3_df$pctlead = 100 * (gspc3_df$leadp - gspc3_df$cp) / gspc3_df$cp
gspc3_df$pctlag1 = c(0, gspc3_df$pctlead)[1:len_i]

# I should get Day-of-Week, Month-of-Year from cdate:
gspc3_df$dow = format(as.Date(gspc3_df$cdate),"%w")
gspc3_df$moy = format(as.Date(gspc3_df$cdate),"%-m")

# I should get rows after 1990-01-01:
pred_v = (as.Date(gspc3_df$cdate) > '1990-01-01')
tail(pred_v)
gspc4_df = gspc3_df[ pred_v , ]

head(gspc4_df)
tail(gspc4_df)

# I should aggregate.


'bye'
