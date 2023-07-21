# minio_delta_lakehouse

# Dependencies
- download the following jar files and place them inside minio-jars folder
    [aws-java-sdk-bundle-1.12.262.jar](https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-bundle)<br>
    [hadoop-aws-3.3.4.jar](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws/3.3.4)

# Run the service
- `docker-compose up`
- use `docker-compose down` when finish using the container

MinIO buckets can be viewed on `localhost:9001` once the containers are running.

You can check if deltalake is connected to Minio storage by accessing `localhost:5000`


# Jupyter Notebook write to MinIO Storage
```
!pip install delta-spark
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
```
