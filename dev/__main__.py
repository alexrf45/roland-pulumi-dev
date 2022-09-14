"""An AWS Python Pulumi program"""

import pulumi
import json
from pulumi_aws import s3
import pulumi_aws as aws

DEV_NAME = 'dev'
DEV_0_NAME = 'dev0'
BUCKET_NAME = 'dev-bucket'


def dev_iam_users():
    """creates two dev users for dev environment"""
    TODO: "generate access tokens and other items"
    dev = aws.iam.User('dev1',
        name = DEV_NAME,
        tags ={
            "name":"dev",
            "group":"dev-team"
        })
    dev_0 = aws.iam.User('dev0',
        name = DEV_0_NAME,
        tags ={
            "name":"dev",
            "group":"dev-team"
        })
    dev_name = pulumi.export('iam_dev_name', dev.name)
    dev0_name = pulumi.export('iam_dev0_name', dev_0.name)

dev_iam_users()

def dev_iam_group():
    """ Creates an IAM group with basic policy. """
    TODO: "implement s3 policy"
    devs = aws.iam.Group('devs',
        path='/')

    dev_test = aws.iam.GroupPolicy('dev-test',
        group = devs.id,
        policy = json.dumps({
            "Version": "2012-10-17",
            "Statement": [{
                "Action": ["ec2:Describe*"],
                "Effect": "Allow",
                "Resource": "*",
            }],
        }))

    dev_team = aws.iam.GroupMembership('dev-team',
        group = devs.id,
        users=[DEV_NAME, DEV_0_NAME])

    pulumi.export('iam_group_name', dev_team.id)

dev_iam_group()


def dev_s3():
    # Create an AWS resource (S3 Bucket)
    bucket = s3.Bucket(BUCKET_NAME,
        acl = "private",
        tags = {
            "Name": "Dev-Bucket",
            "Environment" : "Dev"
        })
    # Export the name of the bucket
    pulumi.export('bucket_name', bucket.id)

dev_s3()

def read_me():
    # open template readme and read contents into stack output
    with open('Pulumi.README.md') as f:
        pulumi.export('readme', f.read())

read_me()

