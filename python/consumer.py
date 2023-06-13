import boto3
import time

session = boto3.Session(region_name='us-east-1')
client = session.client(
    'kinesis',
    aws_access_key_id='',
    aws_secret_access_key='',
    endpoint_url='http://localhost:4567'
)

stream_details = client.describe_stream(StreamName='test_stream')
shard_id = stream_details['StreamDescription']['Shards'][0]['ShardId']

response = client.get_shard_iterator(
    StreamName='test_stream',
    ShardId=shard_id,
    ShardIteratorType='TRIM_HORIZON'
)

shard_iterator = response['ShardIterator']

while True:
    response = client.get_records(ShardIterator=shard_iterator, Limit=5)
    shard_iterator = response['NextShardIterator']
    for record in response['Records']:
        if 'Data' in record and len(record['Data']) > 0:
            print(record['Data'])
    time.sleep(0.75)