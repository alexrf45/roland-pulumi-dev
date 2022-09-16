"""module for s3 bucket creation"""
import pulumi
from pulumi_aws import s3

BUCKET_NAME = 'dev-bucket'
ENVIRONMENT = 'Dev'

def dev_s3():
    '''Create an AWS resource (S3 Bucket)'''
    bucket = s3.Bucket(BUCKET_NAME,
        acl = "private",
        tags = {
            "Name": "Dev-Bucket",
            "Environment" : ENVIRONMENT
        })
    # Export the name of the bucket
    pulumi.export('bucket_name', bucket.id)
    pulumi.export('bucket_name', bucket.bucket_domain_name)
