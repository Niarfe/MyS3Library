import boto3

# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
db = 'dynamodb'
region = 'us-west-2'
table = 'Bookshelf'
fpath = 'library'

dynamodb = boto3.resource(db, region_name=region)
table = dynamodb.Table(table)

def formatter(lines_file_path):
    item = {"Author": "unknown", "Title": str(line) }
    print(item)
    return item

with table.batch_writer() as batch, open(fpath, 'r') as source:
    for line in source:
        batch.put_item(Item = formatter(line))

