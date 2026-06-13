FROM python:3.9-slim

RUN apt-get update && apt-get install -y default-jdk-headless

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY Employee.csv .

CMD ["python", "app.py"]