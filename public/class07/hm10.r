# hm10.r

# Ref:
# https://flowingdata.com/2010/01/21/how-to-make-a-heatmap-a-quick-and-easy-solution/

# Demo:
# R -f hm10.r

# I should load nba data:
#nba = read.csv("http://datasets.flowingdata.com/ppg2008.csv", sep=",")
nba = read.csv("ppg2008.csv", sep=",")
# I should order by PTS column:
nba = nba[order(nba$PTS),]

# I should identify each row by Name instead of an integer:
row.names(nba) = nba$Name

# I should remove the Name column which is the first column:
nba = nba[,2:20]

# I should convert nba to a matrix:
nba_x = data.matrix(nba)

png('hm10.png',width=800, units='px', pointsize=22, height=1100)

heatmap(nba_x, Rowv=NA, Colv=NA, scale="column")

dev.off()
