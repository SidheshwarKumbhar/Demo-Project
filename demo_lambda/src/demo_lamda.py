""""--------------------------------------------------------------------------------------------------------
* The purpose of this demo project is to create lambda function which will get tigger by event pyload
to establish the connection with DynamoDb.

*To achieve the goal of the demo project we will follow the following steps:
    1. Create a function which will connect to the AWS Dynamodb database.
    2. Write the lambda handler which will trigger by the event payload to establish connection with DynamoDB.
    3. Create the test cases for the lambda for the successful and failure scenario.
------------------------------------------------------------------------------------------------------------"""

import boto3    # boto3 allows you to directly create,update and delete the AWS services.
import logging  # logging will help to tracking events that happens when code is runs.

# Create logger, set level and add FileHandler and file format.
logger = logging.getLogger("demo_lambda")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("demo_lamda.log", mode='w')
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info("log for demo_lambda started..")


# The second step of demo project, create the lambda handler function which will get trigger by event to
# establish the connection with DynamoDB.
def lambda_handler(event):
    if event is not None:
        try:
            name = event['Name']
            logger.info("lambda is triggerd by event {}".format(name))

            number = event['Number']
            logger.info("lambda is triggerd by event {}".format(number))

            logger.info("Connecting with DynamoDB")
            return connecting_dynamodb(name, number)

        except KeyError as k:
            # raise KeyError("Error While Connecting to Dynamo DB")
            logger.error("Error While Connecting to Dynamo DB", k)


# The first step of demo project, function which will request to DynamoDB database and create the table in database.
def connecting_dynamodb(name, number):
    try:
        database = boto3.resource('dynamodb')   # requesting for DynamoDb data base
        logger.info("Requested for DynamoDb Services")

        table = database.Table("PhDirectory")  # Table for Phone Directory
        logger.info("A {} Table is Created".format(table))

        elements = table.put_key(           # putting attributes in table for Name and Number Column.
            key={
                'Name': name,
                'Number': number
            }
        )
        logger.info("Attributes {} and {} Added to the table".format(name, number))
        return elements

    except Exception as e:
        # raise Exception("Error While Connecting to Dynamo DB")
        logger.error("Error While Connecting to Dynamo DB", e)
