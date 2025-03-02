import os
import unittest

from pyspark.sql.connect.session import SparkSession

from davidkhala.spark.connect import Databricks


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


class DatabricksTestCase(unittest.TestCase):
    def test_cluster(self):
        cluster_id = "1216-151225-fxmvxmxo"
        token = os.environ['PAT']
        workspace_instance_name = os.environ['WORKSPACE']
        session = Databricks(workspace_instance_name, token, cluster_id)

        df = session.sql('select 1')
        df.show()
        self.assertEqual('Databricks Shell', session.conf.get("spark.app.name"))
        session.stop()


if __name__ == '__main__':
    unittest.main()
