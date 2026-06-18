# Assignment17 -> PySpark Sales Data Processing

This project processes product sales datasets using PySpark inside a Docker container. The application runs automatically when the container starts, sorts all products descending order , display the results & the top 3 products with the highest sales values, and filter products with sales greater than 80,000

## Project Structure
- app.py - The main PySpark application code.
- sales.csv - This dataset contains product sales details.
- Dockerfile - Configuration to install Java, Python, and PySpark.
- requirements.txt - Python dependency file (pyspark).
- output/high_sales_result/ - Output folder containing filtered CSV results.

## How to Build
docker build -t sales-app .

## How to Run
docker run --rm -v "${pwd}:/app" sales-app

## Output

1. Products sorted by sales in descending order
+----------+------------+-----------+------+
|product_id|product_name|   category| sales|
+----------+------------+-----------+------+
|       101|      Laptop|Electronics|150000|
|       103|          TV|Electronics|120000|
|       102|      Mobile|Electronics| 95000|
|       108|         Bed|  Furniture| 90000|
|       106|        Sofa|  Furniture| 80000|
|       105|       Table|  Furniture| 45000|
|       104|       Chair|  Furniture| 30000|
|       107|  Headphones|Electronics| 25000|
+----------+------------+-----------+------+


2. Top 3 products with highest sales
+----------+------------+-----------+------+
|product_id|product_name|   category| sales|
+----------+------------+-----------+------+
|       101|      Laptop|Electronics|150000|
|       103|          TV|Electronics|120000|
|       102|      Mobile|Electronics| 95000|
+----------+------------+-----------+------+


3. Products with sales > 80,000 saved in 'output/high_sales_result' folder