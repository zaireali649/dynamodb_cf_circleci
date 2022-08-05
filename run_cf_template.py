import boto3
import json

with open("dynamodb.json") as parameter_fileobj:
    parameter_data = json.load(parameter_fileobj)

cf = boto3.client('cloudformation')

response = cf.create_stack(
    StackName='DynamoDBSample',
    TemplateBody=json.dumps(parameter_data)
)
