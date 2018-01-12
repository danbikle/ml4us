{
/* ~/sparkapps/logr10/logr12i.scala
This script should download prices and predict daily direction of GSPC.
It should generate a label which I assume to be dependent on price calculations.
A label should classify an observation as down or up. Down is 0.0, up is 1.0.
It should generate independent features from slopes of moving averages of prices.
It should create a Logistic Regression model from many years of features.
Demo:
spark-shell -i logr12i.scala
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

sqls = "SELECT Date, Close, pctlead"
sqls=sqls++",AVG(Close)OVER(ORDER BY Date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS mavg2"
sqls=sqls++",AVG(Close)OVER(ORDER BY Date ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS mavg3"
sqls=sqls++",AVG(Close)OVER(ORDER BY Date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS mavg4"
sqls=sqls++",AVG(Close)OVER(ORDER BY Date ROWS BETWEEN 5 PRECEDING AND CURRENT ROW) AS mavg5"
sqls=sqls++",AVG(Close)OVER(ORDER BY Date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS mavg6"
sqls=sqls++",AVG(Close)OVER(ORDER BY Date ROWS BETWEEN 7 PRECEDING AND CURRENT ROW) AS mavg7"
sqls=sqls++",AVG(Close)OVER(ORDER BY Date ROWS BETWEEN 8 PRECEDING AND CURRENT ROW) AS mavg8"
sqls=sqls++",AVG(Close)OVER(ORDER BY Date ROWS BETWEEN 9 PRECEDING AND CURRENT ROW) AS mavg9"
sqls=sqls++" FROM tab ORDER BY Date"

val dp13df=spark.sql(sqls);dp13df.createOrReplaceTempView("tab")

sqls = "SELECT Date, Close, pctlead"
sqls=sqls++",(mavg2-LAG(mavg2,1)OVER(ORDER BY Date))/mavg2 AS slp2 "
sqls=sqls++",(mavg3-LAG(mavg3,1)OVER(ORDER BY Date))/mavg3 AS slp3 "
sqls=sqls++",(mavg3-LAG(mavg4,1)OVER(ORDER BY Date))/mavg3 AS slp4 "
sqls=sqls++",(mavg3-LAG(mavg5,1)OVER(ORDER BY Date))/mavg3 AS slp5 "
sqls=sqls++",(mavg3-LAG(mavg6,1)OVER(ORDER BY Date))/mavg3 AS slp6 "
sqls=sqls++",(mavg3-LAG(mavg7,1)OVER(ORDER BY Date))/mavg3 AS slp7 "
sqls=sqls++",(mavg3-LAG(mavg8,1)OVER(ORDER BY Date))/mavg3 AS slp8 "
sqls=sqls++",(mavg3-LAG(mavg9,1)OVER(ORDER BY Date))/mavg3 AS slp9 "
sqls=sqls++" FROM tab ORDER BY Date"

val dp14df=spark.sql(sqls);dp14df.createOrReplaceTempView("tab")

// For Class Boundry, I should get avg of pctlead over training period.

val training_period = " WHERE Date BETWEEN'1986-01-01'AND'2015-12-31' "

sqls = "SELECT AVG(pctlead) FROM tab"++training_period

val class_df = spark.sql(sqls)

val class_boundry = class_df.first()(0).asInstanceOf[Double]

// I should compute label from pctlead:

val pctlead2label = udf((pctlead:Float)=> {if (pctlead> class_boundry) 1.0 else 0.0}) 

// I should add the label to my DF of observations:

val dp15df = dp14df.withColumn("label",pctlead2label(col("pctlead")))

dp15df.show

// UNDER CONSTRUCTION
}
