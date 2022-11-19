'''simple module to create an EC2 Instance'''
import pulumi
import pulumi_aws as aws

INSTANCE_TYPE = 't2.micro'
AMI_ID= 'ami-0aa6e9e11c6482f0a'

def instance_dev():
    '''creates a simple security group for instance'''
    group = aws.ec2.SecurityGroup('web-secgrp',
            description='Enable HTTP/HTTPS access',
            ingress=[aws.ec2.SecurityGroupIngressArgs(
                from_port=80,
                to_port=80,
                protocol="tcp",
                cidr_blocks=['0.0.0.0/0'],
            )],
            egress=[aws.ec2.SecurityGroupEgressArgs(
                from_port=80,
                to_port=80,
                protocol="tcp",
                cidr_blocks=["0.0.0.0/0"],
                ipv6_cidr_blocks=["::/0"],
                )],
            tags={
                "Name": "allow_tls",
            })
    user_data = """
    #!/bin/bash
    echo "Hello, World!" > index.html
    nohup python -m SimpleHTTPServer 80 &
    """  
    server = aws.ec2.Instance('web-server-www',
                instance_type=INSTANCE_TYPE,
                vpc_security_group_ids=[group.id],
                user_data=user_data,
                ami=AMI_ID)
    pulumi.export('public_ip', server.public_ip)
    pulumi.export('public_dns', server.public_dns)
