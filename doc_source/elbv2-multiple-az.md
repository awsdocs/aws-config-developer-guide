# elbv2\-multiple\-az<a name="elbv2-multiple-az"></a>

Checks if an Elastic Load Balancer V2 \(Application, Network, or Gateway Load Balancer\) has registered instances from multiple Availability Zones \(AZ's\)\. The rule is NON\_COMPLIANT if an Elastic Load Balancer V2 has instances registered in less than 2 AZ's\. 

**Identifier:** ELBV2\_MULTIPLE\_AZ

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\) Region

**Parameters:**

minAvailabilityZones \(Optional\)Type: int  
Minimum number of expected AZ’s \(between 2 and 10 inclusive\)\.

## AWS CloudFormation template<a name="w79aac11c32c17b7d285c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.