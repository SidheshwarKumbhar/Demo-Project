import boto3

# Lambda Handler
def lambda_handler(event):
    if event is not None:
        try:
            name = event['Name']
            number = event['Number']
        except KeyError as k:
            raise KeyError("Error While Connecting to Dynamo DB")
        return connecting_dynamodb(name, number)

# Connecting to DynamoDB
def connecting_dynamodb(name, number):
    try:
        database = boto3.resource('dynamodb')
        table = database.Table("PhDirectory")    # Table for Phone Directory

        elements = table.put_key(
            key={
                'Name': name,
                'Number': number
            }
        )
        return elements

    except Exception as e:
        raise Exception("Error While Connecting to Dynamo DB")



