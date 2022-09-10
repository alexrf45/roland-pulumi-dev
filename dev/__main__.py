"""An AWS Python Pulumi program"""

import pulumi
import json
from pulumi_aws import s3
import pulumi_aws as aws


policy = aws.iam.Policy("dev_policy",
    name='dev_policy',
    path="/",
    description="development policy",
    policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": ["ec2:Describe*"],
            "Effect": "Allow",
            "Resource": "*",
        }],
    }))
    

pulumi.export('iam_dev_arn', policy.arn)

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('dev')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

# open template readme and read contents into stack output
with open('Pulumi.README.md') as f:
    pulumi.export('readme', f.read())