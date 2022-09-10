import pulumi
import json

import pulumi_aws as aws

def dev_iam_users():
    
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

    
dev_iam_users()

def dev_iam_group():
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

dev_iam_group()