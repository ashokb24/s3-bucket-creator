import boto3


class S3Utils:
    """
        Author: Ashok Bhadrappa
        S3 Utils class to execute my basic work with S3
        -- Creates a bucket
        -- Delete a given bucket
        -- Upload a file to a given path under a given bucket name
        -- remove all the objects under a given bucket name
    """

    def __init__(self, region_name, bucket_name):
        self.region_name = region_name
        self.bucket_name = bucket_name

    def create_s3_bucket(self):
        s3_client = boto3.client('s3', region_name=self.region_name)
        location_constraint_config = {'LocationConstraint': self.region_name}
        s3_client.create_bucket(Bucket=self.bucket_name,
                                CreateBucketConfiguration=location_constraint_config)

    def upload_a_file(self):
        s3_resource = boto3.resource("s3")
        first_object = s3_resource.Object(self.bucket_name, "secrets.txt")
        first_object.upload_file("./secrets.txt", ExtraArgs={'ServerSideEncryption': 'AES256'})


if __name__ == '__main__':
    s3Util = S3Utils("ap-south-1", "my-twitter-secrets-bucket")
    # s3Util.create_s3_bucket()
    # s3Util.upload_a_file()
