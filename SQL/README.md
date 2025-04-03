# User Defined Function (UDF)
- the most useful feature of Spark SQL & DataFrame 
- the most expensive operations: use them only you have no choice and when essential

# Syntax
Insert
- 不能指定要将数据插入哪些列中。这种语句将引发错误`Insert into table_name (taxi_driver_id, first_name) values (3,'Ronda')`
- `INSERT OVERWRITE TABLE ... SELECT ... FROM`可在插入数据的同时清理数据。这让你能够更轻松地重新加载数据
- 

# Spark DataFrame
[wiki](https://github.com/davidkhala/spark/wiki/data-structure)

- DataFrame is not a table/view, so it is anonymous
## Partitioning the output file
When `bikes_df.write.partitionBy("Category").parquet("Files/bike_data")`, it generates folder structure like
```
/bike_data
- /Category=Mountain Bikes
  - ?.parquet
  - ?.parquet
- /Category=Road Bikes
  - ?.parquet
  - ?.parquet
```
> [You can partition the data by multiple columns, which results in a hierarchy of folders for each partitioning key](https://learn.microsoft.com/en-us/training/modules/use-apache-spark-work-files-lakehouse/4-dataframe)

When `road_bikes_df = spark.read.parquet('Files/bike_data/Category=Road Bikes')`
- **omitted**: The results dataframe produced would **not** include a **Category** column


# Temp View
[TempView](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.createTempView.html)
- Scoped to SparkSession. Live in a notebook run 
- common way of sharing data between language

[Global Temp View](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.createOrReplaceGlobalTempView.html)
- Scoped to the cluster. [Live until the cluster stop](https://community.databricks.com/t5/data-engineering/what-s-the-difference-between-a-global-view-and-a-temp-view/m-p/67457/highlight/true#M33344)
