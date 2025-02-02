from pyspark.sql import DataFrame


def show(df: DataFrame):
    from pyspark.sql.streaming import StreamingQuery
    assert df.isStreaming
    df.printSchema()
    query: StreamingQuery = (
        df.writeStream
        .foreachBatch(lambda _df, batch_id: _df.show())
        .start()
    )
    return query
