import unittest

from davidkhala.spark.gcp import AuthOptions


class PubsubTestCase(unittest.TestCase):
    def test_auth(self):
        auth = AuthOptions(clientId='', clientEmail= None, privateKeyId=None, privateKey='')
        print(auth.to_dict())


if __name__ == '__main__':
    unittest.main()
