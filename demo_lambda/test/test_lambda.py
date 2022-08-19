import unittest
from unittest import mock
from demo_lambda.src.demo_lamda import *

# Test Class
class TestDemoLambda(unittest.TestCase):
    # Setup
    def setUp(self):
        self.event = {
            'Name': "sid",
            'Number': 1234567890
        }

    # Tear Down
    def tearDown(self):
        self.event = None

    # Test case for successful run
    def test_lambda(self):
        with mock.patch("demo_lambda.src.demo_lamda.connecting_dynamodb",
                        return_value={'Name': 'Sid', 'Number': 1234567890}):
            response = lambda_handler(self.event)
        self.assertEqual(response, {'Name': 'Sid', 'Number': 1234567890})

    # Test case for Unsuccessful Run
    def test_lambda_for_failure(self):
        with mock.patch("demo_lambda.src.demo_lamda.connecting_dynamodb",
                        return_value={'Name': 'Sidheshwar', 'Number': 1234567890}):
            response = lambda_handler(self.event)
        self.assertNotEqual(response, {'Name': 'Sid', 'Number': 1234567890})


if __name__ == '__main__':
    unittest.main()
