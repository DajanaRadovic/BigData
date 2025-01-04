from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col,lit,desc,avg,count,max as max_, sum as sum_

import matplotlib.pyplot as plt
spark=SparkSession.builder.appName("Job2").getOrCreate()

myFile = "hdfs://localhost:9000/user/hadoop/owid-covid-data.csv"
myData=spark.read.format("csv").option("header","true").option("inferSchema","true").load(myFile)

myDataCorrected=myData.fillna({"icu_patients":"0"}).fillna({"hosp_patients":"0"})
# Izračunavanje ukupnog broja pacijenata po datumu
aggregated_data = (
    myDataCorrected
    .select(col("date"), col("icu_patients"), col("hosp_patients"))
    .withColumn("Total_patients", col("icu_patients") + col("hosp_patients"))
    .groupBy("date")
    .agg(sum_("Total_patients").cast("int").alias("Total num of patients"))
    .orderBy(col("Total num of patients").desc())
)

# Konvertovanje rezultata u Python listu za vizualizaciju
data = aggregated_data.collect()
dates = [row["date"] for row in data]
total_patients = [row["Total num of patients"] for row in data]

# Prikaz samo prvih 5 rezultata
dates = dates[:5]
total_patients = total_patients[:5]

# Vizualizacija pomoću Matplotlib-a
plt.figure(figsize=(10, 6))
plt.bar(dates, total_patients, color='orange')
plt.title("Top 5 Dates with the Highest Number of Patients", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Total Number of Patients", fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()
spark.stop()
