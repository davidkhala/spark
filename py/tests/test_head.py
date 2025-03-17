import datetime
import unittest
from datetime import datetime

from davidkhala.spark.context import Wrapper
from davidkhala.spark.session import regular, ServerMore


class PropertiesTestCase(unittest.TestCase):

    def test_session(self):
        session = regular()
        wrapped = ServerMore(session)
        self.assertEqual("pyspark-shell", wrapped.appName)

    def test_context(self):
        sc = Wrapper.from_config()
        self.assertLess(sc.startTime, datetime.now())
        self.assertEqual('local', sc.master)
        print(sc.defaultParallelism)
        self.assertEqual(1, sc.defaultMinPartitions)
        print(sc.appTime)


class StreamTestCase(unittest.TestCase):
    def test_sample(self):
        from davidkhala.spark.source.stream import sample
        session = regular()
        df = sample(session)
        df.printSchema()



if __name__ == '__main__':
    unittest.main()
