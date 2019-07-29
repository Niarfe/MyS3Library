# Self Getting Started with DynamoDB Went through the [dynamo booklist](https://aws.amazon.com/getting-started/projects/create-manage-nonrelational-database-dynamodb/) tutorial.  Here's my notes for staring a end-2-end walkthrough.

## Sources
* [Link to boto3 docs on dynamo](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)

## Setting up requirements
* Choose your zone, if you don't watch it you can end up creating phantom dbs, `us-west-2`
* Name of your db
* install `pip install boto3`
* obviously, you'll need creds set up etc.

## Create a database
* `create_table.py` is the starting point.
* You need to setup two columns for primary key, first is the HASH, kinda like main group, and then RANGE, (Author/Title)

* `insert_items.py`

* `get_item.py`

## Step 4 in tutorial
* `query_items.py`
* `add_secondary_index.py`
* `query_with_index.py`

## Step 5
* `update_item.py`
 

## Terraform
* Example from [Link:Resource: aws_dynamodb_table](https://www.terraform.io/docs/providers/aws/r/dynamodb_table.html)
* File copied from there, `terra_table.tf`, is an example.  I tried it with my account.
    - Export the AWS keys into the env space first.
    - Note the attributes in the tf file, the two keys are required, but the columns are created with the attributes.

