# Example Relationship Queries<a name="examplerelationshipqueries"></a>

Find EIPs related to an EC2 instance

```
SELECT 
    resourceId 
WHERE 
    resourceType = 'AWS::EC2::EIP'
    AND relationships.resourceId = 'i-abcd1234'
```

Find EIPs related to an EC2 network interface

```
SELECT 
    resourceId 
WHERE 
    resourceType = 'AWS::EC2::EIP' 
    AND relationships.resourceId = 'eni-abcd1234'
```

Find EC2 instances and network interfaces related to a security group

```
SELECT 
    resourceId 
WHERE 
    resourceType IN ('AWS::EC2::Instance', 'AWS::EC2::NetworkInterface') 
    AND relationships.resourceId = 'sg-abcd1234'
```

OR

```
SELECT 
    resourceId 
WHERE 
    resourceType = 'AWS::EC2::Instance' 
    AND relationships.resourceId = 'sg-abcd1234'

SELECT 
    resourceId 
WHERE 
    resourceType = 'AWS::EC2::NetworkInterface' 
    AND relationships.resourceId = 'sg-abcd1234'
```

Find EC2 instances, network ACLs, network interfaces and route tables related to a subnet

```
SELECT 
    resourceId 
WHERE 
    resourceType IN ('AWS::EC2::Instance', 'AWS::EC2::NetworkACL', 'AWS::EC2::NetworkInterface', 'AWS::EC2::RouteTable') 
    AND relationships.resourceId = 'subnet-abcd1234'
```

Find EC2 instances, internet gateways, network ACLs, network interfaces, route tables, subnets and security groups related to a VPC

```
SELECT 
    resourceId 
WHERE 
    resourceType IN ('AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::NetworkACL', 'AWS::EC2::NetworkInterface', 'AWS::EC2::RouteTable', 'AWS::EC2::Subnet', 'AWS::EC2::SecurityGroup') 
    AND relationships.resourceId = 'vpc-abcd1234'
```

Find EC2 route tables related to a VPN gateway

```
SELECT 
    resourceId 
WHERE 
    resourceType = 'AWS::EC2::RouteTable' 
    AND relationships.resourceId = 'vgw-abcd1234'
```