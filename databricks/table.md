[Table types](https://docs.databricks.com/en/tables/index.html#differences-between-delta-tables-streaming-tables-and-materialized-views)

# Delta table
- default table format

## Streaming table
> Does not support the "update" output mode for streaming queries. 
  - You should use the "append" or "complete" output mode instead.
- Only the pipeline that defines the streaming table can update it.


## Online table
Online tables provide lower latency and higher QPS access to data from Delta tables
