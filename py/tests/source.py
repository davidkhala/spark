import unittest

from davidkhala.spark.source.pubsub import GCPAuthOptions


class PubsubTestCase(unittest.TestCase):
    def test_auth(self):
        auth = GCPAuthOptions(clientId='', clientEmail= None, privateKeyId=None, privateKey='')
        print(auth.to_dict())


if __name__ == '__main__':
    unittest.main()
