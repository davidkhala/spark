import datetime
import unittest
from datetime import datetime

from davidkhala.spark.context import getOrCreate
from davidkhala.spark.session import regular, ServerMore


class PropertiesTestCase(unittest.TestCase):

    def test_session(self):
        session = regular()
        wrapped = ServerMore(session)
        self.assertEqual("pyspark-shell", wrapped.appName)
    def test_context(self):
        sc = getOrCreate()
        self.assertLess(sc.startTime, datetime.now())
        self.assertEqual('local[*]', sc.master)
        print(sc.defaultParallelism)
        self.assertEqual(2, sc.defaultMinPartitions)
        print(sc.appTime)

if __name__ == '__main__':
    unittest.main()
