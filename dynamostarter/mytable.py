import boto3

client = boto3.client('dynamodb', region_name='us-west-1')

try:
    resp = client.create_table(
        TableName="Library",
        KeySchema=[
            {
                "AttributeName": "Field",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "Title",
                "KeyType": "RANGE"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "Field",
                "AttributeType": "S"
            },
            {
                "AttributeName": "Title",
                "AttributeType": "S"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )     
    print("Library Table Created!")
except Exception as e:
    print("Error creating table:")
    print(e)

