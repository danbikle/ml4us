# hm_sof1.r

# This script should show a nice demo of a heatmap in R.

# ref:
# http://stackoverflow.com/questions/24621070/heatmap-2-with-color-key-on-top

# I should do this once (similar to pip install):
# install.packages("gplots", repos="http://cran.us.r-project.org")

library(gplots)

png('hm_sof1.png',width=800,height=900)
heatmap.2(x=matrix(rnorm(20*10), nrow=10), Rowv=NULL,Colv=NULL, 
          col = rev(rainbow(20*10, start = 0/6, end = 4/6)), 
          scale="none",
          margins=c(3,0), # ("margin.Y", "margin.X")
          trace='none', 
          symkey=FALSE, 
          symbreaks=FALSE, 
          dendrogram='none',
          density.info='histogram', 
          denscol="black",
          keysize=1, 
          #( "bottom.margin", "left.margin", "top.margin", "left.margin" )
          key.par=list(mar=c(3.5,0,3,0)),
          # lmat -- added 2 lattice sections (5 and 6) for padding
          lmat=rbind(c(5, 4, 2), c(6, 1, 3)), lhei=c(2.5, 5), lwid=c(1, 10, 1))
dev.off()

'bye'
