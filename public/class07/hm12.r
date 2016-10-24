# hm12.r

# This script should generate a heatmap from GSPC dates and prices.
# Ref:
# http://www.tsds4.us/cclasses/class07bk20

# Demo:
# R -f hm12.r

# # I should get GSPC dates and prices:
gspc4_df = read.csv('gspc4.csv')

down_v = (gspc4_df$pctlag1 <  0)
up_v   = (gspc4_df$pctlag1 >= 0)

down0_df = gspc4_df[down_v,]
up0_df   = gspc4_df[up_v,]

# Now I should do down0_df:

# I should use aggregate() to sum(pctlead) groupby Day-of-Week and Month-of-Year:
dowmoy0_df = aggregate(down0_df$pctlead, by=list(dow=down0_df$dow,moy=down0_df$moy),sum)

# I should use better colnames:
colnames(dowmoy0_df) = c('dow','moy','sum_pctlead')

# I should order by dow:
dowmoy1_df = dowmoy0_df[order(dowmoy0_df$dow),]

# Above DF is long and skinny.
# The days are vertically stacked.
# I should slice out each day:
mon = dowmoy1_df[(dowmoy1_df$dow == 1),3]
tue = dowmoy1_df[(dowmoy1_df$dow == 2),3]
wed = dowmoy1_df[(dowmoy1_df$dow == 3),3]
thu = dowmoy1_df[(dowmoy1_df$dow == 4),3]
fri = dowmoy1_df[(dowmoy1_df$dow == 5),3]

# I should horizontally stack the days:
down1_df = data.frame(mon,tue,wed,thu,fri)

# I should build a matrix for a heatmap:
down1_x = data.matrix(down1_df)

# I should write the heatmap to png file:
png('down1.png',width=800, units='px', pointsize=22, height=1100)
down1 = heatmap(down1_x, Rowv=NA, Colv=NA, scale="column",col = rainbow(8, start=0, end=2/6)  )
dev.off()

# Now I should do up0_df:

# I should use aggregate() to sum(pctlead) groupby Day-of-Week and Month-of-Year:
dowmoy0_df = aggregate(up0_df$pctlead, by=list(dow=up0_df$dow,moy=up0_df$moy),sum)

# I should use better colnames:
colnames(dowmoy0_df) = c('dow','moy','sum_pctlead')

# I should order by dow:
dowmoy1_df = dowmoy0_df[order(dowmoy0_df$dow),]

# Above DF is long and skinny.
# The days are vertically stacked.
# I should slice out each day:
mon = dowmoy1_df[(dowmoy1_df$dow == 1),3]
tue = dowmoy1_df[(dowmoy1_df$dow == 2),3]
wed = dowmoy1_df[(dowmoy1_df$dow == 3),3]
thu = dowmoy1_df[(dowmoy1_df$dow == 4),3]
fri = dowmoy1_df[(dowmoy1_df$dow == 5),3]

# I should horizontally stack the days:
up1_df = data.frame(mon,tue,wed,thu,fri)

# I should build a matrix for a heatmap:
up1_x = data.matrix(up1_df)

# I should write the heatmap to png file:
png('up1.png',width=800, units='px', pointsize=22, height=1100)
up1 = heatmap(up1_x, Rowv=NA, Colv=NA, scale="column",col = rainbow(8, start=0, end=2/6)  )
dev.off()

down1_x
up1_x

'bye'
