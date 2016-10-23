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

nba
