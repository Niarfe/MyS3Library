import boto3

client = boto3.client('dynamodb', region_name='us-west-2')

try:
    resp = client.create_table(
        TableName="Bookshelf",
        # Declare your Primary Key in the KeySchema argument
        KeySchema=[{
                "AttributeName": "source",
                "KeyType": "HASH"
            },{
                "AttributeName": "title",
                "KeyType": "RANGE"
            }
        ],
        # The attribute key types are declared here 
        AttributeDefinitions=[{
                "AttributeName": "source",
                "AttributeType": "S"
            },{
                "AttributeName": "title",
                "AttributeType": "S"
            }
        ],
        # ProvisionedThroughput controls the amount of data you can read or write to DynamoDB per second.
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )
    print("Table created successfully!")

except Exception as e:
    print("Error creating table:")
    print(e)
