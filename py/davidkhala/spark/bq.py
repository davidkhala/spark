from pyspark.sql import SparkSession


class PubSub:
    spark: SparkSession

    def read(self, table):
        self.spark.read.format('bigquery').option('table', "adroit-hall-301111.demo.ga4_abt").load()
        # 'your_project.your_dataset.your_table'