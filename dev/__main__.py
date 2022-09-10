"""An AWS Python Pulumi program"""

import pulumi
import json
from pulumi_aws import s3
import pulumi_aws as aws

def dev_iam():
    
    dev = aws.iam.User('dev',
        name='dev',
        tags={
            "name":"dev",
            "group":"dev-team"
        })
    dev_0 = aws.iam.User('dev',
        name='dev0',
        tags={
            "name":"dev",
            "group":"dev-team"
        })

    devs = aws.iam.Group('devs',
        path='/')

    dev_test = aws.iam.GroupPolicy('dev-test',
        group = devs.id,
        policy=json.dumps({
            "Version": "2012-10-17",
            "Statement": [{
                "Action": ["ec2:Describe*"],
                "Effect": "Allow",
                "Resource": "*",
            }],
        }))

    dev_team = aws.iam.GroupMembership('dev-team',
        group = devs.id,
        users=[dev.id, dev_0.id])

    pulumi.export('iam_group_name', dev_team.id)

dev_iam()

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('dev')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

# open template readme and read contents into stack output
with open('Pulumi.README.md') as f:
    pulumi.export('readme', f.read())