from abc import abstractmethod, ABC

from pyspark.sql import DataFrame
from pyspark.sql.streaming import StreamingQuery


class ForeachWriter(ABC):
    def open(self, partition_id, epoch_id):
        # Open connection. This method is optional in Python.
        pass

    @abstractmethod
    def process(self, row):
        # Write row to connection. This method is NOT optional in Python.
        ...

    def close(self, error):
        # Close the connection. This method in optional in Python.
        pass


def show(df: DataFrame):
    assert df.isStreaming

    def on_batch(_df: DataFrame, batch_id):
        # TODO WIP

        import logging
        logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                            filename='new.log',
                            filemode='a')
        logger = logging.getLogger(__name__)
        logger.info(batch_id, _df.count())
        # _df.writeTo('rate_stream').append() # works

    query: StreamingQuery = (
        df.writeStream
        .foreachBatch(on_batch)
        .start()
    )
    return query
