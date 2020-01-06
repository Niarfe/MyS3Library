import boto3
import sys

TABLE_NAME='Bookshelf'

def batch_write(items):
    assert isinstance(items, list)
    assert len(items) > 1
    assert isinstance(items[0], dict)

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    db = dynamodb.Table(TABLE_NAME)
 
    with db.batch_writer() as batch:
       for item in items:
          batch.put_item(Item=item)


def text_list_to_dicts(fname):
    rows = []
    with open(fname, 'r') as source:
        for line in source:
            rows.append({'source':'none', 'title': line.strip()})

    return rows

if __name__ == '__main__':

    fname = sys.argv[1] 

    ldicts = text_list_to_dicts(fname)
    batch_write(ldicts)
    
