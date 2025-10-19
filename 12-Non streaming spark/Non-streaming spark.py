from pyspark.sql import SparkSession 
from pyspark.sql.functions import avg 
import logging 
logger = logging.getLogger('py4j') 
logger.setLevel(logging.ERROR) 
spark = SparkSession.builder \ 
    .appName("WineQualityAnalysis") \ 
    .master("local[*]") \ 
    .getOrCreate() 
spark.sparkContext.setLogLevel("ERROR") 
 
df = spark.read.csv( 
    "file:///home/yuva/Downloads/wine/winequality-red.csv", 
    header=True, 
    inferSchema=True, 
    sep=";" 
) 
 
# Clean column names 
df = df.toDF(*[c.strip().replace(" ", "_").replace("\"", "") for c in df.columns]) 
 
#  First 5 rows 
print("\n--- First 5 Rows ---") 
df.show(5, truncate=False) 
 
#  Distinct quality valuess 
print("\n--- Distinct Quality Values ---") 
df.select("quality").distinct().orderBy("quality").show(truncate=False) 
 
#  Average alcohol by quality 
print("\n--- Average Alcohol by Quality ---") 
result = df.groupBy("quality").agg(avg("alcohol").alias("avg_alcohol")).orderBy("quality") 
result.show(truncate=False) 
 
# Stop Spark 
spark.stop()