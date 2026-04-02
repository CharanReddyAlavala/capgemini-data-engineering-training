from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# start spark
spark = SparkSession.builder.appName("phase3").getOrCreate()

# load data
customers = spark.read.option("header","true").option("inferSchema","true").csv("/samples/customers.csv")
sales = spark.read.option("header","true").option("inferSchema","true").csv("/samples/sales.csv")

# clean data
customers = customers.dropna()
sales = sales.dropna()

# remove invalid rows
sales = sales.filter((col("quantity") > 0) & (col("total_amount") > 0))

# 1 daily sales
daily = sales.groupBy("sale_date").sum("total_amount")
daily.show()

# 2 city revenue
data = sales.join(customers, "customer_id")
city = data.groupBy("city").sum("total_amount")
city.show()

# 3 repeat customers (>2 orders)
repeat = sales.groupBy("customer_id").count().filter("count > 2")
repeat.show()

# 4 top customer in each city
spend = data.groupBy("customer_id","city").sum("total_amount")
w = Window.partitionBy("city").orderBy(desc("sum(total_amount)"))

top = spend.withColumn("rank", rank().over(w)).filter("rank = 1")
top.show()

# 5 final report
report = data.groupBy("customer_id","city").agg(
    sum("total_amount").alias("total_spend"),
    count("*").alias("orders")
)
report.show()
