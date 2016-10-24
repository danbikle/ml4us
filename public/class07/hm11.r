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

# I should compute pctlead,pctlag1 from cp
len_i            = length(gspc3_df$cp)
last_f           = gspc3_df$cp[len_i]
gspc3_df$leadp   = c(gspc3_df$cp, last_f)[1:len_i+1]
gspc3_df$pctlead = 100 * (gspc3_df$leadp - gspc3_df$cp) / gspc3_df$cp
gspc3_df$pctlag1 = c(0, gspc3_df$pctlead)[1:len_i]

# I should get Day-of-Week, Month-of-Year from cdate:
gspc3_df$dow = format(as.Date(gspc3_df$cdate),"%w")
# I should convert moy to integer so I can sort it:
gspc3_df$moy = strtoi(format(as.Date(gspc3_df$cdate),"%-m"))

# I should get rows after 1990-01-01:
pred_v   = (as.Date(gspc3_df$cdate) > '1990-01-01')
gspc4_df = gspc3_df[ pred_v , ]

# I should save this data for other scripts:
write.csv(gspc4_df,'gspc4.csv', row.names=FALSE)

# I should use aggregate() to sum(pctlead) groupby Day-of-Week and Month-of-Year:
dowmoy0_df = aggregate(gspc4_df$pctlead, by=list(dow=gspc4_df$dow,moy=gspc4_df$moy),sum)

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
hm1_df = data.frame(mon,tue,wed,thu,fri)

# I should build a matrix for a heatmap:
hm1_x = data.matrix(hm1_df)

png('hm11.png',width=800, units='px', pointsize=22, height=1100)

hm11 = heatmap(hm1_x, Rowv=NA, Colv=NA, scale="column",col = rainbow(8, start=0, end=2/6)  )

dev.off()

'bye'
