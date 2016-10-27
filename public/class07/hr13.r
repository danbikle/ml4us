# hr13.r

# This script should generate many predictions from dates and prices fed to models.

# Ref:
# http://www.ml4.us/cclasses/class07#hr

# Demo:
# R -f hr12.r

# I should get dates and prices after 2000-01-01

gspc3_df = read.csv('gspc3.csv')

# I should compute pctlead,pctlag1 from cp
len_i            = length(gspc3_df$cp)
last_f           = gspc3_df$cp[len_i]
leadp_v          = c(gspc3_df$cp, last_f)[1:len_i+1]
gspc3_df$pctlead = 100 * (leadp_v - gspc3_df$cp) / gspc3_df$cp
gspc3_df$pctlag1 = c(0, gspc3_df$pctlead)[1:len_i]

# I should get moydow:
gspc3_df$moydow = format(as.Date(gspc3_df$cdate),"%m_%w")

pred_v   = (as.Date(gspc3_df$cdate) > as.Date('2016-09-01'))
gspc4_df = gspc3_df[ pred_v , ]
head(gspc4_df)
tail(gspc4_df)

# I should loop through each date and price:

cdate_v       = gspc4_df$cdate
cp_v          = gspc4_df$cp
moydow_v      = gspc4_df$moydow
pctlag_v      = gspc4_df$pctlag1
predictions_v = c()
row_i         = 0
for (cdate in cdate_v)
{
  row_i = row_i + 1
  # I should get these inputs:
  # yr_test_s, moydow, pctlag_f
  yr_test_s = format(as.Date(cdate),"%Y")
  moydow    = moydow_v[row_i]
  pctlag_f  = pctlag_v[row_i]
  prediction_f  = get_prediction(yr_test_s,moydow,pctlag_f)
  predictions_v = c(predictions_v,c(prediction_f))
}

predictions_v

'bye'
