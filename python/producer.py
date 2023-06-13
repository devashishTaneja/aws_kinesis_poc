import boto3
import json

session = boto3.Session(region_name='us-east-1')
client = session.client(
    'kinesis',
    aws_access_key_id='',
    aws_secret_access_key='',
    endpoint_url='http://localhost:4567'
)

f = open('data.json')
data = json.load(f)

client.put_record(
    StreamName='test_stream',
    Data=json.dumps(data),
    PartitionKey='a'
)