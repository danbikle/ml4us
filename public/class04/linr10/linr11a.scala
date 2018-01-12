{
/*
~/ml4/public/class04/linr10/linr11a.scala
This script should download prices and predict daily direction of GSPC.
It should generate independent features from slopes of moving averages of prices.
It should create a Linear Regression model from many years of features.
Demo:
spark-shell -i linr11a.scala
*/

import org.apache.spark.sql.SQLContext
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.linalg.{Vector, Vectors}
import org.apache.spark.ml.param.ParamMap
import org.apache.spark.sql.Row
import sys.process._

// I should get prices:
"/usr/bin/curl -L ml4.us/csv/GSPC.csv -o /tmp/gspc.csv"!

val sqlContext = new SQLContext(sc)
  
val dp10df = sqlContext
  .read
  .format("com.databricks.spark.csv")
  .option("header","true")
  .option("inferSchema","true")
  .load("/tmp/gspc.csv")

dp10df.createOrReplaceTempView("tab")

spark.sql("SELECT COUNT(Date),MIN(Date),MAX(Date),MIN(Close),MAX(Close)FROM tab").show

// I should compute a label I can use to classify observations.

var sqls="SELECT Date,Close,LEAD(Close,1)OVER(ORDER BY Date) leadp FROM tab ORDER BY Date"

val dp11df=spark.sql(sqls);dp11df.createOrReplaceTempView("tab")

sqls="SELECT Date,Close,100*(leadp-Close)/Close pctlead FROM tab ORDER BY Date"

val dp12df=spark.sql(sqls);dp12df.createOrReplaceTempView("tab")


}
