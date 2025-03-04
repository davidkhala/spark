from typing import Protocol, Optional, Union

from pyspark._globals import _NoValueType, _NoValue


class Catalog(Protocol):
    def currentCatalog(self) -> str:
        ...

    def currentDatabase(self) -> str:
        ...


class RuntimeConf(Protocol):
    def get(
            self, key: str, default: Union[Optional[str], _NoValueType] = _NoValue
    ) -> Optional[str]:
        ...


class SparkSession(Protocol):
    def stop(self) -> None:
        ...

    @property
    def catalog(self) -> Catalog:
        ...

    @property
    def conf(self) -> RuntimeConf:
        ...
    @property
    def readStream(self) -> "DataStreamReader":
        ...