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

# I should compute pctlead from cp
cp_v   = gspc3_df$cp
len_i  = length(cp_v)
last_f = cp_v[len_i]
lead_v = c(cp_v, last_f)[2:len_i]
diff_v = lead_v - cp_v

pctlead_v = 100.0*diff_v / cp_v
head(cp_v)
head(lead_v)
head(diff_v)
head(pctlead_v)
tail(pctlead_v)



'bye'
