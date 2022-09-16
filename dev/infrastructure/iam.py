"""IAM module"""
import json
import pulumi
import pulumi_aws as aws


DEV_NAME = 'dev'
DEV_0_NAME = 'dev0'
DEV_GROUP = 'devs'
ENVIRONMENT = 'Dev'

def dev_iam_users():
    """creates two dev users for dev environment"""
    dev = aws.iam.User('dev1',
        name = DEV_NAME,
        tags ={
            "Name":DEV_NAME ,
            "Group": DEV_GROUP,
            "Environment": ENVIRONMENT
        })
    dev_0 = aws.iam.User('dev0',
        name = DEV_0_NAME,
        tags ={
            "Name": DEV_0_NAME,
            "Nroup": DEV_GROUP,
            "Environment": ENVIRONMENT
        })
    pulumi.export('iam_dev_name' , dev.name)
    pulumi.export('iam_dev0_name', dev_0.name)

# dev_iam_users()

def dev_iam_group():
    """ Creates an IAM group with basic policy. """
    devs = aws.iam.Group(DEV_GROUP, path='/')

    aws.iam.GroupPolicy('dev-test',
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

# dev_iam_group()
