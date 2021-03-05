# fms\-security\-groups\-resource\-association\-check<a name="fms-security-groups-resource-association-check"></a>

Checks whether EC2 or Elastic Network Interface or ALB or ELB associated with FMS security groups\. 

**Identifier:** FMS\_SECURITY\_GROUP\_RESOURCE\_ASSOCIATION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\) Region

**Parameters:**

vpcIdsType: String  
Comma\-separated list of VPC ids in the account\.

securityGroupsIdsType: String  
Comma\-separated list of security groups IDs created by AWS Firewall Manager in every VPC in the account\. Sorted by VPC\.

resourceTagsType: String  
The resource tags \(EC2 Instance or Elastic Network Interface or ALB or ELB\) that the rule should be associated with\. \(for example, \{ "tagKey1" : \["tagValue1"\], "tagKey2" : \["tagValue2", "tagValue3"\] \}

excludeResourceTagsType: boolean  
If true, exclude resources that match resourceTags\.

resourceTypesType: String  
The resource type supported by this rule\. Can be EC2 Instance or Elastic Network Interface or ALB or ELB\.

fmsRemediationEnabledType: boolean  
If true, AWS Firewall Manager will update non\-compliant resources according to FMS policy\. AWS Config ignores this parameter when customer creates this rule\.

exclusiveResourceSecurityGroupManagementFlagType: boolean  
Only allow AWS Firewall Manager created security groups associate with resource if this flag set to true\.

applyToAllEC2InstanceENIs \(Optional\)Type: boolean  
If true, AWS Firewall Manager will enforce the policy on all ENIs on EC2 Instance\. Otherwise AWS Firewall Manager enforce the policy on default ENI on EC2 Instance\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d185c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.