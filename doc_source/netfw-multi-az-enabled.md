# netfw\-multi\-az\-enabled<a name="netfw-multi-az-enabled"></a>

Checks if AWS Network Firewall firewalls are deployed across multiple Availability Zones\. The rule is NON\_COMPLIANT if firewalls are deployed in only one Availability Zone or in fewer zones than the number listed in the optional parameter\. 

**Identifier:** NETFW\_MULTI\_AZ\_ENABLED

**Resource Types:** AWS::NetworkFirewall::Firewall

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

availabilityZones \(Optional\)Type: int  
The number of expected Availability Zones\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d417c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.