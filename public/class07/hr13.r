# hr13.r

# This script should generate many predictions from dates and prices fed to models.

# Ref:
# http://www.ml4.us/cclasses/class07#hr

# Demo:
# R -f hr12.r

# I should get dates and prices after 2000-01-01

gspc3_df = read.csv('gspc3.csv')
pred_v   = (as.Date(gspc3_df$cdate) > as.Date('2016-09-01'))
gspc4_df = gspc3_df[ pred_v , ]
head(gspc4_df)
tail(gspc4_df)

# I should loop through each date and price:

cdate_v = gspc4_df$cdate
cp_v = gspc4_df$cp

row_i = 0
for (cdate in cdate_v)
{
  row_i = row_i + 1
  print(cdate)
  print(cp_v[row_i])
}

'bye'
