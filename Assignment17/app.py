from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("sales-app").getOrCreate()
df = spark.read.csv("sales.csv", header=True, inferSchema=True)


sorted_prod = df.orderBy("sales", ascending=False)
print("\n1. Products sorted by sales in descending order")
sorted_prod.show()


top_3_prod = sorted_prod.limit(3)
print("\n2. Top 3 products with highest sales")
top_3_prod.show()


filtered_prod = df.filter(df["sales"] > 80000)
filtered_prod.write.mode("overwrite").csv("output/high_sales_result", header=True)
print("\n3. Products with sales > 80,000 saved in 'output/high_sales_result' folder")


spark.stop() 