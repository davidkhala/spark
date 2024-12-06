from pyspark.sql import SparkSession

class Regular:
    """
    Visit https://spark.apache.org/docs/latest/sql-getting-started.html#starting-point-sparksession for creating regular Spark Session
    """

    @staticmethod
    def sparkSession():
        return SparkSession.builder.getOrCreate()