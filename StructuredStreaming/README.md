# Streaming dataframe
- Check a dataframe is a streaming dataframe by property `df.isStreaming`
## CRUD
Create
- Create a stream dataframe by `spark.readStream`

Review
- 与普通dataframe不同，你不能直接使用以下操作来查看Streaming DataFrame的内容
  - .show()
  - .collect()
- 使用以下操作来查看Streaming DataFrame的内容
  - foreachBatch: `.writeStream.foreachBatch(lambda df, batch_id: df.show())`
  - persistent them in memory table, and then separately query it by spark.sql() 

Update
```
Operations: Only map-like Dataset/DataFrame operations are supported in continuous mode, that is, only projections (select, map, flatMap, mapPartitions, etc.) and selections (where, filter, etc.).
   All SQL functions are supported except aggregation functions (since aggregations are not yet supported), current_timestamp() and current_date() (deterministic computations using time is challenging).
Sources:
   Kafka source: All options are supported.
   Rate source: Good for testing. Only options that are supported in the continuous mode are numPartitions and rowsPerSecond.
Sinks:
   Kafka sink: All options are supported.
   Memory sink: Good for debugging.
   Console sink: Good for debugging. All options are supported. Note that the console will print every checkpoint interval that you have specified in the continuous trigger.
```
