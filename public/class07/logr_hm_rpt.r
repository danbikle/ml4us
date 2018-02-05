# logr_hm_rpt.r

# This script should help us visualize effectiveness of a Logistic Regression Model.

# Demo:
# R -f logr_hm_rpt.r

my_hm = function(in_x, infn_s){
  # This function should wrap heatmap.2()
  # I should create vectors full of color strings:
  library(gplots)
  col5_v  = rainbow(5, start=0, end=2/6)
  row_i   = length(in_x)
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

  # The above layout has 2 rows and 3 columns.
  # I should specify height of each row:
  row1height_f = 1.8
  row2height_f = 45.0
  lhei_v       = c(row1height_f,row2height_f)
  # I should specify width of each column:
  col1width_f = 1.0
  col2width_f = 9.0
  col3width_f = 2.0
  lwid_v      = c(col1width_f, col2width_f, col3width_f)

  # I should specify available colors and how they sort:
  color_v = rev(rainbow(30, start = 0/6, end = 4/6))
  png(infn_s, width=999, height=7600)
  
  # I should have everything now:
  heatmap.2(x=in_x, Rowv=NULL,Colv=NULL,
    ,col    = color_v
    ,scale  ="none"
    ,margins=c(20.0,1.0) # ("margin.Y", "margin.X")
    ,trace='none' # turns off unneeded trace lines inside the heat map
    ,symkey      =FALSE 
    ,symbreaks   =FALSE 
    ,dendrogram  ='none'
    ,density.info='histogram' 
    ,denscol     ="black"
    ,keysize     =1
    # For color-key at the top:
    #( "bottom.margin", "left.margin", "top.margin", "right.margin" )
    ,key.par =list(mar=c(3.5,0,3,1))
    ,lmat    =lmat_x, lhei=lhei_v, lwid=lwid_v
    ,cexCol  =2.5
    ,cexRow  =1.7
    # I should separate the cells:
    ,sepwidth = c(0.05, 0.1)
    ,rowsep   = c(1:row_i)
    ,colsep   = c(1:2)
    ,xlab     = infn_s
    ,cellnote = round(in_x,1)
    ,notecol  = 'black'
    ,notecex  = 1.8
  )
  dev.off()
}

for (yr_i in c(2000:2017)){
  print('Busy...')
  fn_s = paste('predictions', yr_i, '.csv', sep='')
  pred_df = read.csv(fn_s)[,c('cdate','pctlead','eff')]
  row.names(pred_df) = pred_df$cdate
  pred2_df = pred_df[order(pred_df$eff),]
  pred2_x  = data.matrix(pred2_df[,c('pctlead','eff')])
  colnames(pred2_x) = c('pctlead', 'effectiveness')
  fn2_s = paste('logr_predictions',yr_i, '.png', sep='')
  my_hm(pred2_x, fn2_s)
}

'bye'
