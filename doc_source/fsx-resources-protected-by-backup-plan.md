# fsx\-resources\-protected\-by\-backup\-plan<a name="fsx-resources-protected-by-backup-plan"></a>

Checks if Amazon FSx File Systems are protected by a backup plan\. The rule is NON\_COMPLIANT if the Amazon FSx File System is not covered by a backup plan\. 

**Identifier:** FSX\_RESOURCES\_PROTECTED\_BY\_BACKUP\_PLAN

**Resource Types:** AWS::FSx::FileSystem

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

resourceTags \(Optional\)Type: String  
Tags of Amazon FSx File Systems for the rule to check, in JSON format `{"tagkey" : "tagValue"}`\.

resourceId \(Optional\)Type: String  
ID of the Amazon FSx File System for the rule to check\.

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

## AWS CloudFormation template<a name="w2aac12c33c15b9d325c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.