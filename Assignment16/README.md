# Assignment16 -> PySpark Employee Data Processing

This project processes employee datasets using PySpark inside a Docker container. The application runs automatically when the container starts and saves the results.

## Project Structure
- app.py - The main PySpark application code.
- Employee.csv - This dataset contains employee details.
- Dockerfile - Configuration to install Java, Python, and PySpark.
- requirements.txt - Python dependency file (pyspark).
- top_3_employees_result/ - Output folder created after running the code.

## How to Build
docker build -t emp-app .

## How to Run 
docker run --rm -v "${pwd}:/app" emp-app

# output
output is present in the file -> optput
