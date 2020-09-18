# fms\-security\-group\-content\-check<a name="fms-security-group-content-check"></a>

Checks whether AWS Firewall Manager created security groups content is the same as the master security groups\. The rule is NON\_COMPLIANT if the content does not match\. 

**Note**  
Only AWS Firewall Manager can create this rule\.

**Identifier:** FMS\_SECURITY\_GROUP\_CONTENT\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Middle East \(Bahrain\), Asia Pacific \(Hong Kong\) , Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 vpcIds \(mandatory\)  
Comma\-separated list of VPC IDs in the account\.

 securityGroupsIds \(mandatory\)  
Comma\-separated list of security groups IDs created by Firewall Manager in every Amazon VPC in an account\. They are sorted by VPC IDs\.

 fmsRemediationEnabled \(mandatory\)  
If true, AWS Firewall Manager will update NON\_COMPLIANT resources according to FMS policy\. AWS Config ignores this parameter when you create this rule\. 

revertManualSecurityGroupChangesFlag \(mandatory\)  
If true, AWS Firewall Manager will check the security groups in the securityGroupsIds parameter\. 

 allowSecurityGroup \(mandatory\)  
If true, the rule will check to ensure that all `inScope` security groups are within the reference security group's inbound/outbound rules\.

masterSecurityGroupsIds \(optional\)  
This parameter only applies to AWS Firewall Manager admin account\. Comma\-separated list of master security groups ID in Firewall Manager admin account\.

## AWS CloudFormation template<a name="w22aac11c29c17d181c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.