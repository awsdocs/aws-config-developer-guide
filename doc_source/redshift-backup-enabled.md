# redshift\-backup\-enabled<a name="redshift-backup-enabled"></a>

Checks that Amazon Redshift automated snapshots are enabled for clusters\. The rule is NON\_COMPLIANT if the value for `automatedSnapshotRetentionPeriod` is greater than `MaxRetentionPeriod` or less than `MinRetentionPeriod` or the value is 0\.

**Identifier:** REDSHIFT\_BACKUP\_ENABLED

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

MinRetentionPeriod \(Optional\)Type: int  
Minimum value for the retention period\. Minimum value is 1\.

MaxRetentionPeriod \(Optional\)Type: int  
Maximum value for the retention period\. Maximum value is 35\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d487c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.