# fms\-security\-groups\-audit\-policy\-check<a name="fms-security-groups-audit-policy-check"></a>

Checks if the security groups associated `inScope` resources are compliant with the master security groups at each rule level based on `allowSecurityGroup` and `denySecurityGroup` flag\.

**Note**  
Only AWS Firewall Manager can create this rule\.

**Identifier:** FMS\_SECURITY\_GROUP\_AUDIT\_POLICY\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\) Region

**Parameters:**

masterSecurityGroupsIdsType: String  
Comma\-separated list of master Groups Ids\. Rule will check if security groups associated in scope resource compliant with the master security groups at rule level\.

inScopeType: String  
If true, the config rule owner is in AWS FMS Security Group Audit policy scope\.

resourceTagsType: String  
The resource tags \(EC2 Instance, Elastic Network Interface or Security Group\) that the rule should be associated with\. \(for example, \{ "tagKey1" : \["tagValue1"\], "tagKey2" : \["tagValue2", "tagValue3"\] \}

excludeResourceTagsType: boolean  
If true, exclude resources that match resourceTags\.

resourceTypesType: String  
The resource type supported by this rule\. Can be EC2 Instance, Elastic Network Interface or Security Group\.

fmsRemediationEnabledType: boolean  
If true, AWS Firewall Manager will update non\-compliant resources according to FMS policy\. AWS Config ignores this parameter when customer creates this rule\.

allowSecurityGroupType: boolean  
If true, the rule will check to ensure that all the in\-scope security groups are within \(outside, if false\) the reference security group's inbound/outbound rules\.

## AWS CloudFormation template<a name="w26aac11c31c17b7d181c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.