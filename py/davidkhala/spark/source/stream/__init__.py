from pyspark.sql import SparkSession, DataFrame


def sample(spark: SparkSession, density=1) -> DataFrame:
    return spark.readStream.format('rate').option("rowsPerSecond", density).load()
