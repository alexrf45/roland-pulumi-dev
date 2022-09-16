"""Using the awsx package verus pulumi aws"""
import pulumi
import pulumi_awsx as awsx

CIDR_BLOCK = "10.2.0.0/16"

def dev_vpc():
    """VPC creation function"""
    vpc = awsx.ec2.Vpc("dev-vpc",
        cidr_block = CIDR_BLOCK ,
        number_of_availability_zones = 3,
        subnet_specs=[
            awsx.ec2.SubnetSpecArgs(
            type = awsx.ec2.SubnetType.PRIVATE,
            cidr_mask = 24,
            ),
            awsx.ec2.SubnetSpecArgs(
            type = awsx.ec2.SubnetType.PUBLIC,
            cidr_mask = 24,
            )
        ],
        nat_gateways= awsx.ec2.NatGatewayConfigurationArgs(
            strategy = awsx.ec2.NatGatewayStrategy.SINGLE
        )

    )
    pulumi.export("vpcId", vpc.vpcId)
    pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
    pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
