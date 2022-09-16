"""VPC module to set up seperate VPC"""
import pulumi
import pulumi_aws as aws

VPC_NAME= 'dev-vpc'
NET_NAME='Dev-Network'
ENVIRONMENT='Dev'
CIDR_BLOCK='10.2.0.0/16'
PRIMARY_SUB='10.2.1.0/24'
SECONDARY_SUB='10.2.2.0/24'

def dev_vpc():
    """vpc creation"""
    main = aws.ec2.Vpc(VPC_NAME,
        cidr_block = CIDR_BLOCK,
        enable_dns_support = "True",
        enable_dns_hostnames = "True",
        tags = {
            "Name": NET_NAME,
            "Environment" : ENVIRONMENT
        })


    primary_subnet = aws.ec2.Subnet("dev-test",
        vpc_id = main.id,
        cidr_block = PRIMARY_SUB,
        tags = {
            "Name": NET_NAME,
            "Environment" : ENVIRONMENT
        })

    secondary_subnet = aws.ec2.Subnet("dev-test-1",
        vpc_id = main.id,
        cidr_block = SECONDARY_SUB,
        tags = {
            "Name": NET_NAME,
            "Environment" : ENVIRONMENT
        })
    pulumi.export('owner', main.owner_id)
    pulumi.export('vpc_id', main.id)
    pulumi.export('vpc_tags', main.tags_all)
    pulumi.export('primary_subnet_id', primary_subnet.id)
    pulumi.export('secondary_subnet_id', secondary_subnet.id)
