import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
table = dynamodb.Table('Library')

with table.batch_writer() as batch:
    batch.put_item(Item={"Field": "Language", "Title":"Python Playground", "Category": "Good"})
    batch.put_item(Item={"Field": "Editor", "Title":"Thinking in Vim", "Category": "Tool"})

