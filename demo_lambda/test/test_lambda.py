""""---------------------------------------------------------------------------------------------------------------
The third step of demo project, Create the test cases for the lambda for the successful and failure scenario.

-------------------------------------------------------------------------------------------------------------------"""

import unittest
from unittest import mock   # mock allow you to substitute and imitates the value of function with some dummy value.
from demo_lambda.src.demo_lamda import *

# Create logger, set level and add FileHandler and file format.
logger = logging.getLogger("test_lambda")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("test_lamda.log", mode='w')
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info("log for test_lambda started..")


# Test Class
class TestDemoLambda(unittest.TestCase):
    # Setting up the values for event
    def setUp(self):
        self.event = {
            'Name': "sid",
            'Number': 1234567890
        }
    logger.info("Values for event is set up")

    # Test case for successful run
    def test_lambda(self):
        with mock.patch("demo_lambda.src.demo_lamda.connecting_dynamodb",
                        return_value={'Name': 'Sid', 'Number': 1234567890}):
            response = lambda_handler(self.event)
        self.assertEqual(response, {'Name': 'Sid', 'Number': 1234567890})
    logger.info("test case for the successful run completed.")

    # Test case for Unsuccessful Run
    def test_lambda_for_failure(self):
        with mock.patch("demo_lambda.src.demo_lamda.connecting_dynamodb",
                        return_value={'Name': 'Sidheshwar', 'Number': 1234567890}):
            response = lambda_handler(self.event)
        self.assertNotEqual(response, {'Name': 'Sid', 'Number': 1234567890})
    logger.info("test case for Unsuccessful run completed")

    # Tear Down
    def tearDown(self):
        self.event = None

    logger.info("Values of event is tear Down")


if __name__ == '__main__':
    unittest.main()
