import boto3
import json
from ec2manager import EC2Manager
from s3manager import S3Manager

# this creates a default session using environment variables
# i have exported environment variable for access_key, secret ket and region
# session = boto3.Session(profile_name='chriszano')
session = boto3.Session()


s3 = session.resource('s3')

s3manager = S3Manager(session)
s3manager.list_buckets()

s3manager.upload_file(
    'cdkbasicinfrastack-myfirstbucketb8884501-vsni7jc7yht1', 
    'test.txt', 
    'test.txt'
    )

ec2manager = EC2Manager(session.client('ec2'))
instances = ec2manager.list()

with open('instances.json', 'w') as f:
    json.dump(instances, f, indent=4, default=str, separators=(',', ':'))
