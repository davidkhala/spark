import os
import unittest

from pyspark.sql.connect.session import SparkSession

from davidkhala.spark.connect import Databricks
from davidkhala.spark.sink.stream import show
from davidkhala.spark.source.stream import sample




class LocalTestCase(unittest.TestCase):
    def test_local_master(self):
        session = SparkSession.builder.master("local").getOrCreate()
        # java.io.FileNotFoundException: HADOOP_HOME and hadoop.home.dir are unset
        session.stop()

    def test_local_remote(self):
        self.skipTest('WIp')
        session = (SparkSession.builder
                   .remote("sc://localhost:7077")
                   .getOrCreate())
        session.stop()


def sample_stream_display(spark, density):
    df = sample(spark, density)
    query = show(df)
    query.awaitTermination()


class DatabricksTestCase(unittest.TestCase):
    def setUp(self):
        cluster_id = "1216-151225-fxmvxmxo"
        token = os.environ['PAT']
        workspace_instance_name = os.environ['WORKSPACE']
        self.spark = Databricks(workspace_instance_name, token, cluster_id)

    def test_cluster(self):
        df = self.spark.sql('select 1')
        df.show()
        self.assertEqual('Databricks Shell', self.spark.appName)

    def test_sample(self):
        sample_stream_display(self.spark, 1)

    def tearDown(self):
        self.spark.stop()


if __name__ == '__main__':
    unittest.main()
