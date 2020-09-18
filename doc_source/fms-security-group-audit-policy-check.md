# fms\-security\-group\-audit\-policy\-check<a name="fms-security-group-audit-policy-check"></a>

Checks whether the security groups associated `inScope` resources are compliant with the master security groups at each rule level based on `allowSecurityGroup` and `denySecurityGroup` flag\.

**Note**  
Only AWS Firewall Manager can create this rule\.

**Identifier:** FMS\_SECURITY\_GROUP\_AUDIT\_POLICY\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Middle East \(Bahrain\), Asia Pacific \(Hong Kong\), Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 masterSecurityGroupsIds \(mandatory\)  
Comma\-separated list of master security groups IDs\. The rule will check if security groups associated `inScope` resources are compliant with the master security groups at each rule level\.

 resourceTags \(mandatory\)  
The resource tags associated with the rule \(for example, `{ "tagKey1" : ["tagValue1"], "tagKey2" : ["tagValue2", "tagValue3"] }"`\)\. 

 inScope \(mandatory\)  
If true, the AWS Config rule owner is in Firewall Manager security group audit policy scope\.

 excludeResourceTags \(mandatory\)  
If true, exclude resources that match resourceTags\.

 resourceTypes \(mandatory\)  
The resource types such as Amazon EC2 instance or elastic network interface or security group supported by this rule\. 

 fmsRemediationEnabled \(mandatory\)  
If true, AWS Firewall Manager will update NON\_COMPLIANT resources according to FMS policy\. AWS Config ignores this parameter when you create this rule\. 

 allowSecurityGroup \(mandatory\)  
If true, the rule will check to ensure that all `inScope` security groups are within the reference security group's inbound/outbound rules\.

## AWS CloudFormation template<a name="w22aac11c29c17d179c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.