from abc import abstractmethod, ABC

from pyspark.sql import DataFrame
from pyspark.sql._typing import SupportsProcess, SupportsOpen, SupportsClose
from pyspark.sql.types import Row
from pyspark.sql.streaming import StreamingQuery


class ForeachWriter(SupportsProcess, SupportsOpen, SupportsClose, ABC):
    """
    object class used in DataStreamWriter.foreach(...)
    """

    @abstractmethod
    def process(self, row: Row) -> None: ...


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
