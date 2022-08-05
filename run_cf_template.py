import boto3
import json
import os

with open("dynamodb.json") as parameter_fileobj:
    parameter_data = json.load(parameter_fileobj)

cf = boto3.client('cloudformation',
    region_name='us-east-1',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
    aws_secret_access_key=os.environ['AWS_SECRET_KEY'],)

response = cf.create_stack(
    StackName='DynamoDBSample',
    TemplateBody=json.dumps(parameter_data)
)
