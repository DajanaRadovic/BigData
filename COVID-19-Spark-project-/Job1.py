from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col, lit, max as max_
import matplotlib.pyplot as plt

# Pokretanje Spark sesije
#spark = SparkSession.builder.appName("Job1").getOrCreate()
#spark = SparkSession.builder \
   # .appName("Job1") \
   # .config("spark.master", "local[*]") \
    #.config("spark.executor.memory", "1G") \
    #.config("spark.executor.cores", "1") \
   # .config("spark.driver.memory", "1G") \
    #.getOrCreate()
spark = SparkSession.builder \
    .appName("Job1") \
    .config("spark.executor.memory", "1G") \
    .config("spark.executor.cores", "1") \
    .config("spark.driver.memory", "1G") \
    .getOrCreate()


# Definisanje putanje do CSV fajla
#myFile = "D:/MASTER-2024/BIG-DATA/spark-3.5.3-bin-hadoop3/owid-covid-data.csv"
myFile = "hdfs://192.168.0.19:9000/user/Milijana/owid-covid-data.csv"


# Učitavanje podataka
myData = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(myFile)

# Filtriranje NULL vrednosti u total_cases i continent
myData = myData.filter(col("total_cases").isNotNull())  # Odbacivanje NULL vrednosti u total_cases
myData = myData.filter(col("continent").isNotNull())  # Odbacivanje NULL vrednosti u continent

# Pronalaženje najnovijeg datuma
confrontDate = myData.agg((max_("date").cast("date")).alias("data2")).collect()[0][0]

# Agregacija po kontinentima i prikaz rezultata
agg_Data = myData.select(col("continent"), col("location"), col("total_cases"), col("date")) \
    .withColumn("confront_date", lit(confrontDate)) \
    .filter(col("date") == col("confront_date")) \
    .groupBy("continent") \
    .agg(F.sum("total_cases").cast("int").alias("Number of total cases")) \
    .filter(col("continent").isNotNull()) \
    .orderBy(col("Number of total cases").desc()) 
agg_Data.show()
# Prikupljanje podataka u listu (ova operacija može biti skupa za veliki broj podataka)
results = agg_Data.collect()

# Priprema podataka za grafikon
continents = [row['continent'] for row in results]
total_cases = [row['Number of total cases'] for row in results]

# Vizualizacija pomoću Matplotlib-a
plt.figure(figsize=(10, 6))
plt.bar(continents, total_cases, color='orange')
plt.title('Total Cases by Continent', fontsize=16)
plt.xlabel('Continent', fontsize=14)
plt.ylabel('Total Cases', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Zaustavljanje Spark sesije
spark.stop()

