import boto3

from s3manager import S3Manager

# this creates a default session using environment variables
# i have exported environment variable for access_key, secret ket and region
# session = boto3.Session(profile_name='chriszano')
session = boto3.Session()


s3 = session.resource('s3')

manager = S3Manager(session)

# this would print the bucket names of all the buckets I have
manager.list_buckets()

# this would upload a file to the bucket
manager.upload_file(
    'cdkbasicinfrastack-myfirstbucketb8884501-vsni7jc7yht1', 
    'test.txt', 
    'test.txt'
    )
