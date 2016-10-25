# hm14.r

# This script should generate a heatmap from GSPC dates and prices.
# Ref:
# http://www.tsds4.us/cclasses/class07bk20

# Demo:
# R -f hm14.r

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

gspc2_df           = read.csv('gspc1_df.csv')
gspc3_df           = data.frame(gspc2_df$Date,gspc2_df$Close)
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

# I should get rows after 1990-01-01:
pred_v   = (as.Date(gspc3_df$cdate) > '1990-01-01')
gspc4_df = gspc3_df[ pred_v , ]

# I should get rows where pctlag1 < 0:
down_v = (gspc4_df$pctlag1 < 0)

# I should get rows where pctlag1 >= 0:
up_v = (gspc4_df$pctlag1 >=0)

# I should use aggregate() to sum(pctlead) groupby Month-of-Year, Day-of-Week:
moydow0_d_df = aggregate(pctlead ~ moydow, gspc4_df[down_v,], sum)
moydow0_u_df = aggregate(pctlead ~ moydow, gspc4_df[up_v,  ], sum)

# I should order by moydow descending:
moydow1_d_df   = moydow0_d_df[order(moydow0_d_df$moydow,decreasing=TRUE),]
moydow1_u_df   = moydow0_u_df[order(moydow0_u_df$moydow,decreasing=TRUE),]

# I should hstack them:
d_pctlead = moydow1_d_df$pctlead
u_pctlead = moydow1_u_df$pctlead
moydow_df = data.frame(d_pctlead,u_pctlead)

# I should prepare df for feeding it to heatmap():
row.names(moydow_df) = moydow1_d_df$moydow
moydow_x             = data.matrix(moydow_df)

# I should report:
moydow_x

# I should create vectors full of color strings:
library(gplots)

col5_v  = rainbow(5, start=0, end=2/6)
col60_v = rainbow(nrow(moydow_x), start=0, end=2/6)

# I should write the heatmap to png file:
png('hm14.png',width=1800,height=2800)
hm14 = heatmap.2(moydow_x
  ,dendrogram='none'
  ,scale='column'
  ,Rowv=NA
  ,Colv=NA
  ,col=col5_v
  )
dev.off()

'bye'
