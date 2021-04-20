# elasticache\-redis\-cluster\-auto\-backup\-check<a name="elasticache-redis-cluster-auto-backup-check"></a>

The rule is NON\_COMPLIANT if SnapshotRetentionLimit for Redis cluster is 0, or less than the SnapshotRetentionPeriod parameter\. 

**Identifier:** ELASTICACHE\_REDIS\_CLUSTER\_AUTO\_BACKUP\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

snapshotRetentionPeriod \(Optional\)Type: intDefault: 15  
Minimum snapshot retention period in days for Redis cluster\. Default is 15 days\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d157c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.