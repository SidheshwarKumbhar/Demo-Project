import unittest
from unittest import mock
from demo_lambda.scr.demo_lamda import *

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
        with mock.patch("demo_lambda.scr.demo_lamda.connecting_dynamodb",
                        return_value={'Name': 'Sid', 'Number': 1234567890}):
            response = lambda_handler(self.event)
        self.assertEqual(response, {'Name': 'Sid', 'Number': 1234567890})

    # Test case for Unsuccessful Run
    def test_lambda_for_failure(self):
        with mock.patch("demo_lambda.scr.demo_lamda.connecting_dynamodb",
                        return_value={'Name': 'Sidheshwar', 'Number': 1234567890}):
            response = lambda_handler(self.event)
        self.assertNotEqual(response, {'Name': 'Sid', 'Number': 1234567890})

    # Test Case for Checking  Exception in Lambda
    def test_lambda_for_Exception(self):
        with self.assertRaises(Exception) as k:
            lambda_handler(self.event)
        self.assertEqual(str(k.exception), "Error While Connecting to Dynamo DB")

    # Test Case for Checking Exception While Connecting DynamoDB
    def test_lambda_for_Exception_in_connecting_dynamodb(self):
        with self.assertRaises(Exception) as e:
            lambda_handler(self.event)
        self.assertEqual(str(e.exception), "Error While Connecting to Dynamo DB")


if __name__ == '__main__':
    unittest.main()
