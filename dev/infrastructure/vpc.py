"""VPC module to set up seperate VPC"""
import pulumi
import pulumi_aws as aws

VPC_NAME= 'dev-vpc'
NET_NAME='Dev-Network'
PRIMARY_NET_NAME = 'Dev-Network-001'
SECONDARY_NET_NAME = 'Dev-Network-002'
ENVIRONMENT='Dev'
PUBLIC_CIDR_BLOCK='10.2.0.0/16'
PRIMARY_SUB='10.2.1.0/24'
SECONDARY_SUB='10.2.2.0/24'

def dev_vpc():
    """vpc creation"""
    main = aws.ec2.Vpc(VPC_NAME,
        cidr_block = PUBLIC_CIDR_BLOCK,
        enable_dns_support = "True",
        enable_dns_hostnames = "True",
        tags = {
            "Name": NET_NAME,
            "Environment" : ENVIRONMENT
        })


    primary_subnet = aws.ec2.Subnet("dev-test",
        vpc_id = main.id,
        cidr_block = PRIMARY_SUB,
        map_public_ip_on_launch = "True",
        tags = {
            "Name": PRIMARY_NET_NAME,
            "Environment" : ENVIRONMENT
        })

    secondary_subnet = aws.ec2.Subnet("dev-test-1",
        vpc_id = main.id,
        cidr_block = SECONDARY_SUB,
        tags = {
            "Name": SECONDARY_NET_NAME,
            "Environment" : ENVIRONMENT
        })
    i_gw = aws.ec2.InternetGateway("dev-ig-gw",
        vpc_id = main.id,
        tags = {
            "Name": NET_NAME,
            "Environment" : ENVIRONMENT
        })
    pulumi.export('owner', main.owner_id)
    pulumi.export('vpc_id', main.id)
    pulumi.export('ig_gwid', i_gw.id)
    pulumi.export('vpc_tags', main.tags_all)
    pulumi.export('primary_subnet_id', primary_subnet.id)
    pulumi.export('secondary_subnet_id', secondary_subnet.id)
    return primary_subnet.id
