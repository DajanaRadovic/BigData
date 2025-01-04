from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col,lit,desc,avg,count,max as max_

import matplotlib.pyplot as plt

spark=SparkSession.builder.appName("Job2").getOrCreate()

myFile = "hdfs://localhost:9000/user/hadoop/owid-covid-data.csv"
myData=spark.read.format("csv").option("header","true").option("inferSchema","true").load(myFile)

newTestsCorrected=myData.fillna({"new_tests":"0"})
#newTestsCorrected.select(col("location"),col("new_tests"))\
#.groupBy("location").agg((avg("new_tests").cast("int")).alias("Average number of new tests"))\
#.orderBy(col("location")).show(newTestsCorrected.count())
# Agregacija prosečnog broja novih testova po lokaciji
result = (
    newTestsCorrected.select(col("location"), col("new_tests"))
    .groupBy("location")
    .agg((avg("new_tests").cast("int")).alias("Average number of new tests"))
    .orderBy(col("location"))
)

# Konvertovanje rezultata u listu za vizualizaciju
data = result.collect()  # Pretvara Spark DataFrame u listu redova
locations = [row["location"] for row in data]
average_tests = [row["Average number of new tests"] for row in data]

# Vizualizacija pomoću Matplotlib-a
plt.figure(figsize=(15, 8))
plt.bar(locations, average_tests, color='blue')
plt.title("Average Number of New Tests per Location", fontsize=16)
plt.xlabel("Location", fontsize=14)
plt.ylabel("Average Number of New Tests", fontsize=14)
plt.xticks(rotation=90, fontsize=8)
plt.tight_layout()
plt.show()
spark.stop()
