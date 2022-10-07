"""An AWS Python Pulumi program
dev_vpc()
    - Creates a VPC with two subnets
dev_iam_users()
    - Creates two iam users, dev and dev0

dev_iam_group()
    - Creates simple iam group,
    - Attaches a sample policy to it
    - Adds dev and dev0 to the group

dev_s3()
    - Creates a single s3 bucket

read_me()
    - Creates read me for pulumi dashboard
"""
import sys
from time import sleep
from infrastructure.vpc import dev_vpc
# from infrastructure.vpc1 import dev_vpc
from infrastructure.iam import dev_iam_group, dev_iam_users
from infrastructure.s3 import dev_s3
from infrastructure.ec2 import dev_ec2
from documentation.readme import read_me

sys.path.append('./dev')

dev_vpc()

dev_iam_users()

dev_iam_group()

dev_s3()

dev_ec2()

sleep(2)

read_me()
