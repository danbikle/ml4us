# hm11.r

# This script should generate a heatmap from GSPC dates and prices.
# Ref:
# http://www.tsds4.us/cclasses/class07bk20

# Demo:
# R -f hm11.r

# I should get GSPC dates and prices:
gspc0_df = read.csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
head(gspc0_df)
write.csv(gspc0_df,'gspc0_df.csv')

'bye'
