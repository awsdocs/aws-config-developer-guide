# fms\-security\-group\-resource\-association\-check<a name="fms-security-group-resource-association-check"></a>

Checks whether Amazon EC2 or an elastic network interface is associated with AWS Firewall Manager security groups\. The rule is NON\_COMPLIANT if the resources are not associated with FMS security groups\. 

**Note**  
Only AWS Firewall Manager can create this rule\.

**Identifier:** FMS\_SECURITY\_GROUP\_RESOURCE\_ASSOCIATION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Middle East \(Bahrain\), Asia Pacific \(Hong Kong\), Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 vpcIds \(mandatory\)  
Comma\-separated list of VPC IDs in the account\.

 securityGroupsIds \(mandatory\)  
Comma\-separated list of security groups IDs created by Firewall Manager in every Amazon VPC in an account\. They are sorted by VPC IDs\.

 resourceTags \(mandatory\)  
The resource tags such as Amazon EC2 instance or elastic network interface associated with the rule \(for example, `{ "tagKey1" : ["tagValue1"], "tagKey2" : ["tagValue2", "tagValue3"] }"`\)\. 

 excludeResourceTags \(mandatory\)  
If true, exclude resources that match resourceTags\.

 resourceTypes \(mandatory\)  
The resource types such as Amazon EC2 instance or elastic network interface or security group supported by this rule\. 

 fmsRemediationEnabled \(mandatory\)  
If true, AWS Firewall Manager will update NON\_COMPLIANT resources according to FMS policy\. AWS Config ignores this parameter when you create this rule\. 

exclusiveResourceSecurityGroupManagementFlag \(mandatory  
If true, only allows AWS Firewall Manager created security groups associated with resource\.

## AWS CloudFormation template<a name="w22aac11c29c17d183c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.