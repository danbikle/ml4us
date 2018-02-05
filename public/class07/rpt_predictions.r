# rpt_predictions.r

# This script should read predictions.csv and report 
# -Long-Only Effectiveness
# -Model Effectiveness
# -Long-Only Accuracy
# -Model Accuracy

# Demo:
# R -f rpt_predictions.r

# I should read predictions.csv
predictions_df = read.csv('predictions.csv')

# I should report Long-Only Effectiveness:
long_only_eff_f = sum(predictions_df$pctlead)
print('long_only_eff:')
print(long_only_eff_f)

# I should calculate Model Effectiveness.
# Logic should be:
# If prediction has same sign as pctlead, that prediction is both effective and accurate:
predictions_df$effectiveness = sign(predictions_df$prediction) * predictions_df$pctlead

# I should report Model Effectiveness:
model_eff_f = sum(predictions_df$effectiveness)
print('model_eff:')
print(model_eff_f)

# I should calculate Long-Only Accuracy.
pctlead_up_v = sign(predictions_df$pctlead)
# I should count the 1 values
lo_count_up_i = sum(pctlead_up_v == 1)
# Accuracy should be count of up days divided by all days:
lo_accuracy_f = 100.0 * lo_count_up_i / length(predictions_df$pctlead)
print('Long-Only accuracy:')
print(lo_accuracy_f)

# I should calculate model Accuracy.
# If the signs match, that should be accurate:
predictions_df$accuracy = sign(predictions_df$prediction) * sign(predictions_df$pctlead)

# I should count the 1 values
tf_v = (predictions_df$accuracy == 1)
# I should use sum() to sum the 1 values which should be same as count of TRUE values.
true_count_i = sum(tf_v)
all_count_i  = length(predictions_df$accuracy)
accuracy_f   = 100.0 * true_count_i / all_count_i
print('model accuracy:')
print(accuracy_f)

# I should setup some data for heatmap.2
pred1_v      = (as.Date(predictions_df$cdate) > '2018-01-01')
pred2_v      = (as.Date(predictions_df$cdate) < '2019-01-01')
pred3_v      = pred1_v & pred2_v
pred2018a_df = predictions_df[pred3_v , c('cdate','pctlead') ]
pred2018b_df = pred2018a_df[order(pred2018a_df$pctlead),]
pred2018b_df

# I should convert pred2018b_df to a matrix:
row.names(pred2018b_df) = pred2018b_df$cdate
pred2018b_x             = data.matrix(pred2018b_df)
pred2018b_x
pred2018c_x = pred2018b_x[ , c(2,2)]

row_i = length(pred2018c_x)

# I should create vectors full of color strings:
library(gplots)

col5_v  = rainbow(5, start=0, end=2/6)
col60_v = rainbow(row_i, start=0, end=2/6)

# I should prep the layout for the heatmap.

# A default heatmap layout has 4 things:
# - Color Key, which is like a legend
# - Column Dendrogram, which I usually dont want
# - Row Dendrogram,    which I usually dont want
# - Heatmap,           which I always want
# A default heatmap layout is controlled by 4 integers: 4,3,2,1
# I use variables instead of integers:
colorKey_i  = 4
colDendro_i = 3
rowDendro_i = 2
heatmap_i   = 1
# I like to add margins and each margin needs an integer:
margin_left5_i = 5
margin_left6_i = 6

# I want the layout to look like this:
# -----------------------------------------------
# | margin_left5 | colorKey | colDendro(unused) |
# | margin_left6 | heatmap  | rowDendro(unused) |
# -----------------------------------------------

# I should use above integers to create a layout_matrix:
lmat_x = rbind(c(margin_left5_i, colorKey_i, colDendro_i)
              ,c(margin_left6_i, heatmap_i,  rowDendro_i))

lmat_x

# The above layout has 2 rows and 3 columns.
# I should specify height of each row:
row1height_f = 0.8
row2height_f = 5.0
lhei_v       = c(row1height_f,row2height_f)
# I should specify width of each column:
col1width_f = 1.0
col2width_f = 10.0
col3width_f = 1.0
lwid_v      = c(col1width_f, col2width_f, col3width_f)

# I should specify available colors and how they sort:
color_v = rev(rainbow(30, start = 0/6, end = 4/6))

png('rpt_predictions.png',width=900, height=1600)

# I should see the matrix fed to the heatmap:
pred2018c_x

heatmap.2(x=pred2018c_x, Rowv=NULL,Colv=NULL,
  ,col    = color_v
  ,scale  ="none"
  ,margins=c(25.0,0.0) # ("margin.Y", "margin.X")
  ,trace='none' # turns off unneeded trace lines inside the heat map
  ,symkey      =FALSE 
  ,symbreaks   =FALSE 
  ,dendrogram  ='none'
  ,density.info='histogram' 
  ,denscol     ="black"
  ,keysize     =1
  # For color-key at the top:
  #( "bottom.margin", "left.margin", "top.margin", "right.margin" )
  ,key.par =list(mar=c(3.5,0,3,0))
  ,lmat=rbind(c(5, 4, 2), c(6, 1, 3)), lhei=c(2.5, 5), lwid=c(1, 10, 1)
)
#   
#   ,lmat    =lmat_x, lhei=lhei_v, lwid=lwid_v
# )
#   ,cexCol  =2.0
#   ,cexRow  =2.0
#   # I should separate the cells:
#   ,sepcolor='white'
#   ,sepwidth=c(0.1, 0.1)
#   ,rowsep  =c(1:row_i)
#   ,colsep  =c(1:2)
#   ,xlab    = 'Effectiveness Color Map Visualization'
#   ,cellnote = round(pred2018c_x,1)
#   ,notecol  = 'black'
#   ,notecex  = 1.8
# )

dev.off()

'bye'
