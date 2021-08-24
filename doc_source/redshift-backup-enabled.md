# redshift\-backup\-enabled<a name="redshift-backup-enabled"></a>

Checks that Amazon Redshift automated snapshots are enabled for clusters\. The rule is NON\_COMPLIANT if the value for `automatedSnapshotRetentionPeriod` is greater than `MaxRetentionPeriod` or less than `MinRetentionPeriod` or the value is 0\.

**Identifier:** REDSHIFT\_BACKUP\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Ningxia\), Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

MinRetentionPeriod \(Optional\)Type: int  
Minimum value for the retention period\. Minimum value is 1\.

MaxRetentionPeriod \(Optional\)Type: int  
Maximum value for the retention period\. Maximum value is 35\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d309c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.