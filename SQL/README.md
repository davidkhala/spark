## User Defined Function (UDF)
- the most useful feature of Spark SQL & DataFrame 
- the most expensive operations: use them only you have no choice and when essential

## Spark DataFrame
[wiki](https://github.com/davidkhala/spark/wiki/data-structure)


- DataFrame is not a table/view, so it is anonymous
### Temp View
[TempView](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.createTempView.html)
- Scoped to SparkSession. Live in a notebook run 
- common way of sharing data between language

[Global Temp View](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.createOrReplaceGlobalTempView.html)
- Scoped to the cluster. [Live until the cluster stop](https://community.databricks.com/t5/data-engineering/what-s-the-difference-between-a-global-view-and-a-temp-view/m-p/67457/highlight/true#M33344)
