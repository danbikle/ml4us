# hm10.r

# Ref:
# https://flowingdata.com/2010/01/21/how-to-make-a-heatmap-a-quick-and-easy-solution/

# Demo:
# R -f hm10.r

# I should load nba data:
#nba <- read.csv("http://datasets.flowingdata.com/ppg2008.csv", sep=",")
nba <- read.csv("ppg2008.csv", sep=",")
# I should order by PTS column:
nba <- nba[order(nba$PTS),]

# I should identify each row by Name instead of an integer:
row.names(nba) <- nba$Name

# I should remove the Name column which is the first column:
nba = nba[,2:20]

# I should convert nba to a matrix:
nba_matrix = data.matrix(nba)

# I should call heatmap():
# hm10 = heatmap(nba_matrix)
# hm11 = heatmap(nba_matrix, Rowv=NA, Colv=NA, col = cm.colors(256), scale="column", margins=c(5,10))

png('hm10.png',width=800, units='px', pointsize=22, height=1100)

hm12 = heatmap(nba_matrix, Rowv=NA, Colv=NA, scale="column",col = rainbow(8, start=0, end=2/6)  )

dev.off()



