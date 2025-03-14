from abc import abstractmethod, ABC
from typing import Callable

from pyspark.sql import DataFrame
from pyspark.sql.streaming import StreamingQuery
from pyspark.sql.types import Row


class ForeachWriter(ABC):

    """
    object class used in DataStreamWriter.foreach(...)
    """

    def open(self, partition_id: int, epoch_id: int) -> bool: ...
    @abstractmethod
    def process(self, row: Row) -> None: ...

    def close(self, error: Exception) -> None: ...

def show(df: DataFrame, on_batch: Callable[[DataFrame, int], None]):
    assert df.isStreaming

    query: StreamingQuery = df.writeStream.foreachBatch(on_batch).start()
    return query
