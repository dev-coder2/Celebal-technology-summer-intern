# Import necessary PySpark functions
from pyspark.sql.functions import col, sum as spark_sum, desc, unix_timestamp, window

# Load NYC taxi data
file_path = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv"

# Read CSV into a PySpark DataFrame
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(file_path)

# Show the schema to understand the data structure
df.printSchema()

# Query 1: Add a column named "Revenue" which is the sum of specific columns
df = df.withColumn("Revenue", col("Fare_amount") + col("Extra") + col("MTA_tax") + col("Improvement_surcharge") + col("Tip_amount") + col("Tolls_amount") + col("Total_amount"))
df.select("Revenue").show()

# Query 2: Increasing count of total passengers in New York City by area
passenger_count_by_area = df.groupBy("pickup_location_id").agg(spark_sum("passenger_count").alias("total_passengers")).orderBy("total_passengers", ascending=False)
passenger_count_by_area.show()

# Query 3: Real-time average fare/total earning amount earned by 2 vendors
avg_fare_by_vendor = df.groupBy("vendor_id").agg({"Fare_amount": "avg", "Revenue": "sum"}).withColumnRenamed("avg(Fare_amount)", "Average_Fare").withColumnRenamed("sum(Revenue)", "Total_Earnings")
avg_fare_by_vendor.show(2)

# Query 4: Moving count of payments made by each payment mode
payment_count = df.groupBy("payment_type").count().withColumnRenamed("count", "payment_count")
payment_count.show()

# Query 5: Highest two gaining vendors on a particular date with number of passengers and total distance by cab
date = "2020-01-01"  # Example date
highest_gaining_vendors = df.filter(df.tpep_pickup_datetime.contains(date)).groupBy("vendor_id").agg(spark_sum("Revenue").alias("total_revenue"), spark_sum("passenger_count").alias("total_passengers"), spark_sum("trip_distance").alias("total_distance")).orderBy(desc("total_revenue")).limit(2)
highest_gaining_vendors.show()

# Query 6: Most number of passengers between a route of two locations
most_passengers_route = df.groupBy("pickup_location_id", "dropoff_location_id").agg(spark_sum("passenger_count").alias("total_passengers")).orderBy(desc("total_passengers"))
most_passengers_route.show(1)

# Query 7: Get top pickup locations with most passengers in the last 5/10 seconds
# Add a timestamp column
df = df.withColumn("timestamp", unix_timestamp("tpep_pickup_datetime"))

# Define the window duration (5 or 10 seconds)
window_duration = "5 seconds"  # or "10 seconds"

# Group by pickup location and window to get the count of passengers
top_pickup_locations = df.groupBy(window(col("timestamp"), window_duration), "pickup_location_id").agg(spark_sum("passenger_count").alias("total_passengers")).orderBy(desc("total_passengers"))
top_pickup_locations.show()
