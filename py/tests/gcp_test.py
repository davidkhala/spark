import os
import unittest

from davidkhala.gcp.auth import OptionsInterface
from davidkhala.gcp.auth.options import from_service_account

from davidkhala.spark.gcp import AuthOptions

auth = AuthOptions(
    clientId=os.environ.get('CLIENT_ID'),
    privateKey=os.environ.get('PRIVATE_KEY'),
    clientEmail=os.environ.get('CLIENT_EMAIL'),
    privateKeyId=os.environ.get('PRIVATE_KEY_ID'),
    projectId=os.environ.get('PROJECT_ID'),
)


class CommonTestCase(unittest.TestCase):

    def test_auth(self):
        _ = from_service_account(
            client_email=auth.get('clientEmail'),
            private_key=auth.get('privateKey'),
            project_id=auth.get('projectId'),
        )
        OptionsInterface.token.fget(_)


if __name__ == '__main__':
    unittest.main()
