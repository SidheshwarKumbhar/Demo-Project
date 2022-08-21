import boto3
import logging

logger = logging.getLogger("demo_lambda")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("demo_lamda.log", mode='w')
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info("log for demo_lambda started..")


# Lambda Handler
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


# Connecting to DynamoDB
def connecting_dynamodb(name, number):
    try:
        database = boto3.resource('dynamodb')
        logger.info("Requested for DynamoDb Services")

        table = database.Table("PhDirectory")  # Table for Phone Directory
        logger.info("A {} Table is Created".format(table))

        elements = table.put_key(
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
