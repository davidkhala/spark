import os
import unittest

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.compute import PythonPyPiLibrary
from davidkhala.databricks.workspace.server import Library
from pyspark.sql import SparkSession as RegularSparkSession
from pyspark.sql.connect.session import SparkSession

from davidkhala.spark.session import ServerMore, Databricks
from davidkhala.spark.sink.stream import startAny
from davidkhala.spark.sink.stream.vendor import NewRelic
from davidkhala.spark.source.stream import sample


class LocalTestCase(unittest.TestCase):
    def test_local_master(self):
        session = RegularSparkSession.builder.master("local").getOrCreate()
        # java.io.FileNotFoundException: HADOOP_HOME and hadoop.home.dir are unset
        session.stop()

    def test_local_remote(self):
        self.skipTest('WIP')
        session = (SparkSession.builder.remote("sc://localhost:7077").getOrCreate())
        session.stop()


def sample_stream_display(spark, density):
    df = sample(spark, density)

    query = startAny(df, NewRelic())
    query.awaitTermination()


class DatabricksTestCase(unittest.TestCase):
    spark: ServerMore

    @classmethod
    def setUpClass(cls):
        cluster_id = os.environ.get('CLUSTER_ID')
        token = os.environ.get('PAT')
        workspace_instance_name = os.environ.get('WORKSPACE')
        library = Library(WorkspaceClient(host=workspace_instance_name, token=token, cluster_id=cluster_id))
        library.add(PythonPyPiLibrary(package='davidkhala-devops[new-relic]'))

        cls.spark = Databricks(workspace_instance_name, token, cluster_id)

    def test_cluster(self):
        df = self.spark.sql('select 1')
        self.assertEqual('Databricks Shell', self.spark.appName)
        df.show()

    def test_sample(self):
        if os.environ.get('CI') == 'true':
            self.skipTest('run forever')
        sample_stream_display(self.spark, 1)

    @classmethod
    def tearDownClass(cls):
        cls.spark.disconnect()


if __name__ == '__main__':
    unittest.main()
