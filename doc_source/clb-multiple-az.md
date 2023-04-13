# clb\-multiple\-az<a name="clb-multiple-az"></a>

Checks if a Classic Load Balancer spans multiple Availability Zones \(AZs\)\. The rule is NON\_COMPLIANT if a Classic Load Balancer spans less than 2 AZs or does not span number of AZs mentioned in the `minAvailabilityZones` parameter \(if provided\)\. 

**Identifier:** CLB\_MULTIPLE\_AZ

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), China \(Ningxia\) Region

**Parameters:**

minAvailabilityZones \(Optional\)Type: int  
Desired minimum number of expected AZs\. Valid values are between 2 and 10, both inclusive\. Default value is 2 if parameter is not specified\.

## AWS CloudFormation template<a name="w2aac12c33c15b9c77c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.