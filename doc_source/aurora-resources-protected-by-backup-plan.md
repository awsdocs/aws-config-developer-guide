# aurora\-resources\-protected\-by\-backup\-plan<a name="aurora-resources-protected-by-backup-plan"></a>

Checks if Amazon Aurora DB clusters are protected by a backup plan\. The rule is NON\_COMPLIANT if the Amazon Relational Database Service \(Amazon RDS\) Database Cluster is not protected by a backup plan\. 

**Identifier:** AURORA\_RESOURCES\_PROTECTED\_BY\_BACKUP\_PLAN

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

resourceTags \(Optional\)Type: String  
Tags of Aurora DB clusters for the rule to check, in JSON format\.

resourceId \(Optional\)Type: String  
ID of Aurora DB cluster for the rule to check\.

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

## AWS CloudFormation template<a name="w79aac11c32c17b9c35c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.