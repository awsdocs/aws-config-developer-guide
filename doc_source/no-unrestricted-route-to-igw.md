# no\-unrestricted\-route\-to\-igw<a name="no-unrestricted-route-to-igw"></a>

Checks if there are public routes in the route table to an Internet Gateway \(IGW\)\. The rule is NON\_COMPLIANT if a route to an IGW has a destination CIDR block of '0\.0\.0\.0/0' or '::/0' or if a destination CIDR block does not match the rule parameter\. 

**Identifier:** NO\_UNRESTRICTED\_ROUTE\_TO\_IGW

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Osaka\) Region

**Parameters:**

routeTableIds \(Optional\)Type: CSV  
Comma\-separated list of route table IDs that can have routes to an Internet Gateway with a destination CIDR block of '0\.0\.0\.0/0' or '::/0'\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d257c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.