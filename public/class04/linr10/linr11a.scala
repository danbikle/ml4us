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
import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.linalg.{Vector, Vectors}
import org.apache.spark.ml.param.ParamMap
import org.apache.spark.sql.Row
import sys.process._

// I should declare training_period, test_period

val training_period = " WHERE Date BETWEEN'1986-01-01'AND'2016-01-01' "
val test_period     = " WHERE Date BETWEEN'2016-01-01'AND'2017-01-01' "

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

// I should declare a dependent variable: "pctlead".
// If it truely is dependent that makes it predictable.

var sqls="SELECT Date,Close,LEAD(Close,1)OVER(ORDER BY Date) leadp FROM tab ORDER BY Date"

val dp11df=spark.sql(sqls);dp11df.createOrReplaceTempView("tab")

sqls="SELECT Date,Close,100*(leadp-Close)/Close pctlead FROM tab ORDER BY Date"

val dp12df=spark.sql(sqls);dp12df.createOrReplaceTempView("tab")

// I should now collect features AKA independent variables.

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

// In Linear Regression, I should use pctlead as the label:
  
sqls = "SELECT Date, Close, pctlead, pctlead label "
sqls=sqls++",(mavg2-LAG(mavg2,1)OVER(ORDER BY Date))/mavg2 AS slp2 "
sqls=sqls++",(mavg3-LAG(mavg3,1)OVER(ORDER BY Date))/mavg3 AS slp3 "
sqls=sqls++",(mavg4-LAG(mavg4,1)OVER(ORDER BY Date))/mavg4 AS slp4 "
sqls=sqls++",(mavg5-LAG(mavg5,1)OVER(ORDER BY Date))/mavg5 AS slp5 "
sqls=sqls++",(mavg6-LAG(mavg6,1)OVER(ORDER BY Date))/mavg6 AS slp6 "
sqls=sqls++",(mavg7-LAG(mavg7,1)OVER(ORDER BY Date))/mavg7 AS slp7 "
sqls=sqls++",(mavg8-LAG(mavg8,1)OVER(ORDER BY Date))/mavg8 AS slp8 "
sqls=sqls++",(mavg9-LAG(mavg9,1)OVER(ORDER BY Date))/mavg9 AS slp9 "
sqls=sqls++" FROM tab ORDER BY Date"

val dp15df=spark.sql(sqls)

// I should copy slp-values into Vectors.dense():

val fill_vec = udf((
  slp2:Float
  ,slp3:Float
  ,slp4:Float
  ,slp5:Float
  ,slp6:Float
  ,slp7:Float
  ,slp8:Float
  ,slp9:Float
  )=> {Vectors.dense(
  slp2
  ,slp3
  ,slp4
  ,slp5
  ,slp6
  ,slp7
  ,slp8
  ,slp9
  )
  }
)

val dp16df = dp15df.withColumn("features"
,fill_vec(
  col("slp2")
  ,col("slp3")
  ,col("slp4")
  ,col("slp5")
  ,col("slp6")
  ,col("slp7")
  ,col("slp8")
  ,col("slp9")
  )
)

// I should gather observations to learn from:
dp16df.createOrReplaceTempView("tab")

// I should create a LinearRegression instance. This instance is an 'Estimator'.

val lr = new LinearRegression()

lr.setMaxIter(1234).setRegParam(0.01)

// I should gather observations to learn from:
dp16df.createOrReplaceTempView("tab")

val train_df = spark.sql("SELECT * FROM tab"++training_period)

/*I should fit a LinearRegression model to observations.
This uses the parameters stored in lr.*/

val model1 = lr.fit(train_df)

val test_df = spark.sql("SELECT * FROM tab"++test_period)

/* I should predict. It is convenient that predictions_df will contain a copy of test_df.*/

val predictions_df = model1.transform(test_df)
predictions_df.createOrReplaceTempView("tab")

// eff logic
val eff = udf((pctlead:Float,prediction:Double)=> {if (prediction>0) pctlead else -pctlead})

// prediction report:
val p2df = predictions_df.withColumn("effectiveness",eff(col("pctlead"),col("prediction")))

println("Predictions Report:")
p2df.select("Date","Close","pctlead","effectiveness","label","prediction").show(255)

// I should report in a way which is consistent with the python script linr11a.py:

// I should get Linear Regression Accuracy:
sqls = "SELECT COUNT(Date) pc FROM tab WHERE (prediction>0 AND pctlead>0)OR(prediction<=0 AND pctlead<=0)"

val pc_df = spark.sql(sqls)

val poscount_i = pc_df.first()(0).asInstanceOf[Long]

sqls = "SELECT COUNT(Date) rcount FROM tab"

val rc_df = spark.sql(sqls)

val rcount_i = rc_df.first()(0).asInstanceOf[Long]

println("Linear Regression Accuracy:")
println(poscount_i.toFloat/rcount_i)

// I should get Long-Only Accuracy:
sqls = "SELECT COUNT(Date) upcount FROM tab WHERE pctlead>0"

val upcount_df = spark.sql(sqls)
val upcount_i  = upcount_df.first()(0).asInstanceOf[Long]

println("Long Only Accuracy:")
println(upcount_i.toFloat/rcount_i)

val tp_df = spark.sql("SELECT COUNT(Date) tpc FROM tab WHERE prediction>0 AND pctlead>0")
println("True Positive Count:")
tp_df.show

val fp_df = spark.sql("SELECT COUNT(Date) fpc FROM tab WHERE prediction>0 AND pctlead<0")
println("False Positive Count:")
fp_df.show

val tn_df = spark.sql("SELECT COUNT(Date) tnc FROM tab WHERE prediction<=0 AND pctlead<=0")
println("True Negative Count:")
tn_df.show

val fn_df = spark.sql("SELECT COUNT(Date) fnc FROM tab WHERE prediction<=0 AND pctlead>0")
println("False Negative Count:")
fn_df.show

println("Effectiveness of negative predictions:")
spark.sql("SELECT -SUM(pctlead) eff_np FROM tab WHERE prediction<=0").show

println("Effectiveness of positive predictions:")
spark.sql("SELECT SUM(pctlead) eff_pp FROM tab WHERE prediction>0").show

println("Effectiveness of Long-Only-Model:")
spark.sql("SELECT SUM(pctlead) eff_lo FROM tab").show

}
