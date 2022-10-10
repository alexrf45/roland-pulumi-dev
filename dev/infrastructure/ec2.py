''' Creates and EC2 instance with a basic security group
and exports the public IP and publichostname'''
import pulumi
import pulumi_aws as aws


SIZE = 't2.micro'
AMI = 'ami-0f01974d5fd3b4530'
SUBNET = aws.ec2.get_subnet(filters=[aws.ec2.GetSubnetFilterArgs(
    name="tag:Name",
    values=["Dev-Network-001"],
)])

def dev_ec2():
    '''EC2 Function'''
    # ubuntu = aws.ec2.get_ami_ids(filters=[aws.ec2.GetAmiIdsFilterArgs(
    #     name="name",
    #     values=["ubuntu/images/ubuntu-*-*-amd64-server-*"],
    #     )],
    # owners=["amazon"],
    # sort_ascending = "True"
    # )
    group = aws.ec2.SecurityGroup('dev-instance-sec-grp',
        description='Enable HTTP access',
        ingress=[
            { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0'] }
        ])

    server = aws.ec2.Instance('dev-instance',
    instance_type = SIZE,
    vpc_security_group_ids = [group.id], # reference security group from above
    ami=AMI,
    subnet_id=SUBNET.id)

    pulumi.export('publicIp', server.public_ip)
    pulumi.export('publicHostName', server.public_dns)
