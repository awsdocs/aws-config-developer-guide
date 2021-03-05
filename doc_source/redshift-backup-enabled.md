# redshift\-backup\-enabled<a name="redshift-backup-enabled"></a>

Checks that Amazon Redshift automated snapshots are enabled for clusters\. 

**Identifier:** REDSHIFT\_BACKUP\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Ningxia\), Asia Pacific \(Sydney\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

MinRetentionPeriod \(Optional\)Type: int  
Minimum value for the retention period\. Minimum value is 1\.

MaxRetentionPeriod \(Optional\)Type: int  
Maximum value for the retention period\. Maximum value is 35\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d271c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.