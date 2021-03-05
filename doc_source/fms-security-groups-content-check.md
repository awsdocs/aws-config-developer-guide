# fms\-security\-groups\-content\-check<a name="fms-security-groups-content-check"></a>

Check whether the security groups content is the same as the master security group\. 

**Identifier:** FMS\_SECURITY\_GROUP\_CONTENT\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\) Region

**Parameters:**

vpcIdsType: String  
Comma\-separated list of VPC ids in the account\.

securityGroupsIdsType: String  
Comma\-separated list of security groups IDs created by AWS Firewall Manager in every VPC in the account\. Sorted by VPC ids\.

fmsRemediationEnabledType: boolean  
If true, AWS Firewall Manager will update non\-compliant resources according to FMS policy\. AWS Config ignores this parameter when customer creates this rule\.

revertManualSecurityGroupChangesFlagType: boolean  
If true, AWS Firewall Manager will check the security groups in the securityGroupsIds parameter\.

masterSecurityGroupsIds \(Optional\)Type: String  
This parameter only applies to AWS Firewall Manager admin account\. Comma\-separated list of master security groups id in AWS Firewall manager admin account\. Rule will check if the AWS Firewall manager created security groups in the account are same as the master security groups\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d183c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.