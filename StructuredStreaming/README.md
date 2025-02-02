Streaming dataframe
- Check a dataframe is a streaming dataframe by property `df.isStreaming`
- Create a stream dataframe by `spark.readStream`
- 与普通dataframe不同，你不能直接使用以下操作来查看Streaming DataFrame的内容
  - .show()
  - .collect()
- 使用以下操作来查看Streaming DataFrame的内容
  - foreachBatch: `.writeStream.foreachBatch(lambda df, batch_id: df.show())`
  - persistent them in memory table, and then separately query it by spark.sql() 
  
