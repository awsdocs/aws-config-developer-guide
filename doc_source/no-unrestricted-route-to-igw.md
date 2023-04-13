# no\-unrestricted\-route\-to\-igw<a name="no-unrestricted-route-to-igw"></a>

Checks if route tables have inputs other than these default values: CIDR block of ‘0\.0\.0\.0/0’ as the Destination for IPv4 or ‘::/0’ for IPv6, and ‘igw\-id’ as the Target\. The rule is NON\_COMPLIANT if you keep defaults\.

**Identifier:** NO\_UNRESTRICTED\_ROUTE\_TO\_IGW

**Resource Types:** AWS::EC2::RouteTable

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

routeTableIds \(Optional\)Type: CSV  
Comma\-separated list of route table IDs that can have routes to an Internet Gateway with a destination CIDR block of '0\.0\.0\.0/0' or '::/0'\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d429c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.