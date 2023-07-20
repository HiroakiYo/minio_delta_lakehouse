from flask import Flask
import pyspark
from delta import *

builder = pyspark.sql.SparkSession.builder.appName("MyApp") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .config("spark.jars.packages","org.apache.hadoop:hadoop-aws:3.3.4") \
    .config("spark.hadoop.fs.s3a.access.key","minio_access_key") \
    .config("spark.hadoop.fs.s3a.secret.key", "minio_secret_key") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://172.24.0.10:9000") \
    .config("spark.databricks.delta.retentionDurationCheck.enabled","false") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
spark = configure_spark_with_delta_pip(builder).getOrCreate()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Backend on Docker Container is Running!</p>"

@app.route("/write_test")
def write_test():
    spark.range(100).write.format("delta").mode("overwrite").save("s3a://delta-lake/demo1")
    df = spark.read.format("delta").load("s3a://delta-lake/demo1")
    result = ""
    rows = df.collect()
    for row in rows:
        result += str(row['id'])
        result += "\n"
    return "Write Finished\n" + str(result)