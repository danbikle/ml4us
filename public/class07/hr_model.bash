#!/bin/bash

# hr_model.bash

# This script should collect data and feed it to a heuristic model.

# Then it should report on the effectiveness of the model by comparing predictions to observations.

# I should start by getting data and generating a CSV file full of features:
R -f genf.r

# Next, I should create a series of models for a series of years:
R -f hr_model.r
# The above script should create some CSV files with names like these:

# dan@acer2:~/ml4us/public/class07 $ 
# dan@acer2:~/ml4us/public/class07 $ ll model2*csv
# -rw-rw-r-- 1 dan dan 1141 Oct 29 19:26 model2000.csv
# -rw-rw-r-- 1 dan dan 1133 Oct 29 19:26 model2001.csv
# -rw-rw-r-- 1 dan dan 1144 Oct 29 19:26 model2002.csv
# -rw-rw-r-- 1 dan dan 1147 Oct 29 19:26 model2003.csv
# -rw-rw-r-- 1 dan dan 1145 Oct 29 19:26 model2004.csv
# -rw-rw-r-- 1 dan dan 1144 Oct 29 19:26 model2005.csv
# -rw-rw-r-- 1 dan dan 1138 Oct 29 19:26 model2006.csv
# -rw-rw-r-- 1 dan dan 1135 Oct 29 19:26 model2007.csv
# -rw-rw-r-- 1 dan dan 1135 Oct 29 19:26 model2008.csv
# -rw-rw-r-- 1 dan dan 1151 Oct 29 19:26 model2009.csv
# -rw-rw-r-- 1 dan dan 1155 Oct 29 19:26 model2010.csv
# -rw-rw-r-- 1 dan dan 1160 Oct 29 19:26 model2011.csv
# -rw-rw-r-- 1 dan dan 1153 Oct 29 19:26 model2012.csv
# -rw-rw-r-- 1 dan dan 1143 Oct 29 19:26 model2013.csv
# -rw-rw-r-- 1 dan dan 1153 Oct 29 19:26 model2014.csv
# -rw-rw-r-- 1 dan dan 1156 Oct 29 19:26 model2015.csv
# -rw-rw-r-- 1 dan dan 1150 Oct 29 19:26 model2016.csv
# dan@acer2:~/ml4us/public/class07 $ 
# dan@acer2:~/ml4us/public/class07 $ 
# dan@acer2:~/ml4us/public/class07 $


# Then, I should use the above files to help me generate predictions:
R -f get_predictions.r
# The above script should create some CSV files with names like these:

# dan@acer2:~/ml4us/public/class07 $ 
# dan@acer2:~/ml4us/public/class07 $ ll predictions*v
# -rw-rw-r-- 1 dan dan  27307 Oct 29 19:12 predictions2000.csv
# -rw-rw-r-- 1 dan dan  26870 Oct 29 19:12 predictions2001.csv
# -rw-rw-r-- 1 dan dan  27136 Oct 29 19:12 predictions2002.csv
# -rw-rw-r-- 1 dan dan  27132 Oct 29 19:12 predictions2003.csv
# -rw-rw-r-- 1 dan dan  27491 Oct 29 19:12 predictions2004.csv
# -rw-rw-r-- 1 dan dan  27545 Oct 29 19:12 predictions2005.csv
# -rw-rw-r-- 1 dan dan  27397 Oct 29 19:12 predictions2006.csv
# -rw-rw-r-- 1 dan dan  27300 Oct 29 19:12 predictions2007.csv
# -rw-rw-r-- 1 dan dan  27131 Oct 29 19:12 predictions2008.csv
# -rw-rw-r-- 1 dan dan  27059 Oct 29 19:12 predictions2009.csv
# -rw-rw-r-- 1 dan dan  27356 Oct 29 19:12 predictions2010.csv
# -rw-rw-r-- 1 dan dan  27280 Oct 29 19:12 predictions2011.csv
# -rw-rw-r-- 1 dan dan  27291 Oct 29 19:12 predictions2012.csv
# -rw-rw-r-- 1 dan dan  27430 Oct 29 19:12 predictions2013.csv
# -rw-rw-r-- 1 dan dan  27520 Oct 29 19:12 predictions2014.csv
# -rw-rw-r-- 1 dan dan  27436 Oct 29 19:12 predictions2015.csv
# -rw-rw-r-- 1 dan dan  22780 Oct 29 19:12 predictions2016.csv
# -rw-rw-r-- 1 dan dan 328782 Oct 29 19:27 predictions.csv
# dan@acer2:~/ml4us/public/class07 $ 
# dan@acer2:~/ml4us/public/class07 $ 

# Next, I should report effectiveness:
R -f rpt_predictions.r

# I should see something like this:

# > # rpt_predictions.r
# > 
# > # This script should report the effectiveness of predictions in predictions.csv
# > 
# > # Demo:
# > # R -f rpt_predictions.r
# > 
# > # I should read predictions.csv
# > 
# > predictions_df = read.csv('predictions.csv')
# > 
# > # I should report Long-Only Effectiveness:
# > sum(predictions_df$pctlead)
# [1] 70.96948
# > 
# > # I should calculate Model Effectiveness
# > predictions_df$effectiveness = sign(predictions_df$prediction) * predictions_df$pctlead
# > head(predictions_df)
#        cdate      cp     pctlead     pctlag1 moydow moy dow prediction
# 1 2000-01-03 1455.22 -3.83446682 -0.95491094   01_1   1   1       5.96
# 2 2000-01-04 1399.42  0.19221827 -3.83446682   01_2   1   2       3.74
# 3 2000-01-05 1402.11  0.09556782  0.19221827   01_3   1   3      12.25
# 4 2000-01-06 1403.45  2.70903996  0.09556782   01_4   1   4       9.87
# 5 2000-01-07 1441.47  1.11899695  2.70903996   01_5   1   5      20.43
# 6 2000-01-10 1457.60 -1.30625119  1.11899695   01_1   1   1      -1.26
#   effectiveness
# 1   -3.83446682
# 2    0.19221827
# 3    0.09556782
# 4    2.70903996
# 5    1.11899695
# 6    1.30625119
# > 
# > # I should report Model Effectiveness:
# > sum(predictions_df$effectiveness)
# [1] 41.99261
# > 
# > 'bye'
# [1] "bye"
# > 
# dan@acer2:~/ml4us/public/class07 $ 
# dan@acer2:~/ml4us/public/class07 $ 
# dan@acer2:~/ml4us/public/class07 $


# The above report tells me that although the model offers positive effectiveness,
# 41.99% from 2000 through 2016-10-27,
# the Long-Only Model gives a higher effectiveness of 70.97%.
