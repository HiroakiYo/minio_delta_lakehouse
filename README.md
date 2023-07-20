# minio_delta_lakehouse

# Dependencies
- download the following jar files and place them inside minio-jars folder
    [aws-java-sdk-bundle-1.12.262.jar](https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-bundle)<br>
    [hadoop-aws-3.3.4.jar](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws/3.3.4)

# Run the service
- `docker-compose up`
- use `docker-compose down` when finish using the container

MinIO buckets can be viewed on [localhost:9001](localhost:9001) once the containers are running.

You can check if deltalake is connected to Minio storage by accessing [localhost:5000](localhost:5000)
