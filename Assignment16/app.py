from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("spark-app-1").getOrCreate()

df = spark.read.csv("Employee.csv", header=True, inferSchema=True)

sorted_df = df.orderBy("salary", ascending=False)
print("\n1: Employees sorted by salary")
sorted_df.show()

dept_totals = df.groupBy("department").sum("salary")
print("\n2: Department wise total")
dept_totals.show()


top_3_df = sorted_df.limit(3)
top_3_df.write.csv("top_3_employees_result", header=True)
print("\n3: Top 3 employees saved in 'top_3_employees_result' folder")

spark.stop()