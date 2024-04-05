# Create VPC
Name: MyVPC
IPv4 CIDR Block: 10.0.0.0/16

### Create Public Subnets ###

# Public Subnet 1
Name: Public-Subnet1-A
Availability Zone: us-east-1a
IPv4 CIDR Block: 10.0.1.0/24

# Public Subnet 2
Name: Public-Subnet2-B
Availability Zone: us-east-1b
IPv4 CIDR Block: 10.0.2.0/24

# Private Subnet 1
Name: Private-Subnet1-A
Availability Zone: us-east-1a
IPv4 CIDR Block: 10.0.3.0/24

# Private Subnet 2
Name: Private-Subnet2-B
Availability Zone: us-east-1b
IPv4 CIDR Block: 10.0.4.0/24

# Create public route table

Name: Public-Router
VPC: MyVPC
Subnet associations: Public-Subnet1-A, Public-Subnet2-B

# Create Internet Gateway

Name: MyIGW
VPC: MyVPC