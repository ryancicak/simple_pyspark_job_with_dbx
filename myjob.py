from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.getOrCreate()

# Create example data
data = [("Alice", 1), ("Bob", 2)]
columns = ["name", "value"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Write DataFrame to the Unity Catalog table: cicak_tester.default.test_table
df.write.mode("append").saveAsTable("cicak_tester.default.test_table")

print("Table written successfully!")

