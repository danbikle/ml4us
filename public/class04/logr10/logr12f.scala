{
/* ~/sparkapps/logr10/logr12f.scala
This script should download prices and predict daily direction of GSPC.
It should generate a label which I assume to be dependent on price calculations.
A label should classify an observation as down or up. Down is 0.0, up is 1.0.
It should generate independent features from slopes of moving averages of prices.
It should create a Logistic Regression model from many years of features.
Demo:
spark-shell -i logr12f.scala
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

val dp12df=spark.sql(sqls)

dp12df.show

// UNDER CONSTRUCTION
}
