class S3Manager:
    def __init__(self, session) -> None:
        self.s3 = session.resource('s3')
        
    def list_buckets(self):
        for bucket in self.s3.buckets.all():
            print(bucket.name)    
    def upload_file(self, bucket_name, file_name, object_name):
        self.s3.Bucket(bucket_name).upload_file(file_name, object_name)