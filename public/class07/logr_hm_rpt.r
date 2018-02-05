# logr_hm_rpt.r

# This script should help us visualize effectiveness of a Logistic Regression Model.

# Demo:
# R -f logr_hm_rpt.r

for (yr_i in c(2000:2017)){
  fn_s = paste('predictions', yr_i, '.csv', sep='')
  pred_df = read.csv(fn_s)[,c('cdate','pctlead','eff')]
  row.names(pred_df) = pred_df$cdate
  pred2_x  = data.matrix(pred_df[,c('pctlead','eff')])
  colnames(pred2_x) = c('pctlead', 'effectiveness')
  print(head(pred2_x))
}

'bye'
