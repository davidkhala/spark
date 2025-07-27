
`UNION`
- 在SQL(包括Spark SQL？)中，union和union all是不同的
- 但在PySpark Dataframe [API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.unionAll.html)中，`unionAll() is an alias to union()`，结果与SQL中的union all相同，都不去重

NULL value process
- `df.dropna()`: 删除所有至少有一列为NULL的行
  - `.dropna('all')`: 只删除全空的行
  - `.dropna(how='any', subset = ['badQualityColumn'])`: 只删除指定列为NULL的行
- `df.fillna()`: 将NULL替换为固定值（仅在列类型匹配时才执行替换）
- Imputer: 拟合插值工具，只能用于double或者float
  - `from pyspark.ml.feature import Imputer`
  - default `strategy='mean'`

DeDup
- 使用window function `row_number()` 配合 `filter()`
- `df.dropDuplicates(...)`

broadcast join
- 将dimension table的备份发送到每个节点上
- 通常是在幕后进行的
- explicitly: `df.join(broadcast(df_dimension), ...)`


read parquet
- ```
  SELECT * FROM parquet.`<dir_path>`  
  ```

`PIVOT`: rotates rows into columns.
- transform data from a long format (rows representing individual measurements) to a wide format (columns representing multiple measurements)
- effectively reshape a table
- ```
  SELECT *
  FROM (
    SELECT date, metric_type, value
    FROM sensor_data
  ) PIVOT (
    MAX(value) FOR metric_type IN ('temperature', 'humidity', 'pressure')
  )

  ```
- reverse: `UNPIVOT`
