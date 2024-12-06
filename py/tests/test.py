import importlib
import unittest


class CommonTestCase(unittest.TestCase):
    def test_import(self):
        common = importlib.import_module('davidkhala.spark')
        from davidkhala.spark import Regular
        self.assertTrue(isinstance(common.Regular(), Regular))




if __name__ == '__main__':
    unittest.main()
