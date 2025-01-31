from pyspark import SparkConf
from pyspark.errors import IllegalArgumentException
from pyspark.sql import SparkSession

class Wrapper:
    spark: SparkSession

    def __init__(self, spark):
        self.spark: SparkSession = spark

    def disconnect(self):
        self.spark.stop()

    @property
    def schema(self) -> str:
        """
        :return: current schema full name
        """
        return self.spark.catalog.currentCatalog() + '.' + self.spark.catalog.currentDatabase()

    def __getattr__(self, name):
        # Delegate unknown attributes/methods to the wrapped instance
        return getattr(self.spark, name)
class Regular(Wrapper, SparkSession):
    @property
    def appName(self):
        try:
            return self.spark.conf.get("spark.app.name")
        except IllegalArgumentException as e:
            if str(e).splitlines()[0] == "The value of property spark.app.name must not be null":
                return
            else:
                raise e
def regular(*, name: str = None, conf: SparkConf = SparkConf())->Regular:
    """
    Visit https://spark.apache.org/docs/latest/sql-getting-started.html#starting-point-sparksession for creating regular Spark Session
    """
    _ = SparkSession.builder.config(conf=conf)
    if name: _.appName(name)

    return Regular(_.getOrCreate())