import datetime
import importlib
import unittest

from pyspark import SparkContext

from spark.session import regular, Wrapper
from spark.context import Wrapper as SCWrapper, getOrCreate
from datetime import datetime
class SyntaxTestCase(unittest.TestCase):
    def test_import(self):
        common = importlib.import_module('davidkhala.spark')

        self.assertTrue(isinstance(common.Decorator(), Wrapper))

    def test_session(self):
        session = regular()
        self.assertTrue(isinstance(session.sparkContext, SparkContext))
        self.assertEqual("pyspark-shell", session.appName)
    def test_context(self):
        sc = getOrCreate()
        self.assertLess(sc.startTime, datetime.now())
        self.assertEqual('local[*]', sc.master)
        print(sc.defaultParallelism)
        self.assertEqual(2, sc.defaultMinPartitions)
        print(sc.appTime)

if __name__ == '__main__':
    unittest.main()
