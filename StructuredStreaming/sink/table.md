```python

df.writeStream.format("delta").option("checkpointLocation", checkpointpath).start(output_table_path)

```
option `checkpointLocation` is required
> The `checkpointLocation` option is used to write a checkpoint file that tracks the state of the stream processing.
> This file enables you to recover from failure at the point where stream processing left off.

When finished, stop the streaming data to avoid unnecessary processing costs: `query.stop()`

