import unittest

from pyspark.sql.connect.session import SparkSession


class ConnectTestCase(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
