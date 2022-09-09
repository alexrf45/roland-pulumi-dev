"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3
import pulumi_awsx as awsx

vpc = awsx.ec2.DefaultVpc("default-vpc")

pulumi.export("vpc_id", vpc.vpc_id)

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('test-roland')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

# open template readme and read contents into stack output
with open('./Pulumi.README.md') as f:
    pulumi.export('readme', f.read())