# ec2\-resources\-protected\-by\-backup\-plan<a name="ec2-resources-protected-by-backup-plan"></a>

Checks if Amazon Elastic Compute Cloud \(Amazon EC2\) instances are protected by a backup plan\. The rule is NON\_COMPLIANT if the Amazon EC2 instance is not covered by a backup plan\.

**Note**  
This rule is only applicable to running Amazon EC2 instances and not to instances that are powered down\.

**Identifier:** EC2\_RESOURCES\_PROTECTED\_BY\_BACKUP\_PLAN

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

resourceTags \(Optional\)Type: String  
Tags for Amazon EC2 instances for the rule to check, in JSON format `{"tagkey" : "tagValue"}`\.

resourceId \(Optional\)Type: String  
ID of Amazon EC2 instance for the rule to check\.

crossRegionList \(Optional\)Type: String  
Comma\-separated list of destination regions for the cross\-region backup copy to be kept

crossAccountList \(Optional\)Type: String  
Comma\-separated list of destination accounts for cross\-account backup copy to be kept

maxRetentionDays \(Optional\)Type: int  
The maximum retention period in days for the Backup Vault Lock

minRetentionDays \(Optional\)Type: int  
The minimum retention period in days for the Backup Vault Lock

backupVaultLockCheck \(Optional\)Type: String  
Accepted values: 'True' or 'False'\. Enter 'True' for the rule to check if the resource is backed up in a locked vault

## AWS CloudFormation template<a name="w2aac12c31c27b9d207c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.