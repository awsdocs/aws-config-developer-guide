# elasticache\-redis\-cluster\-automatic\-backup\-check<a name="elasticache-redis-cluster-automatic-backup-check"></a>

The rule is NON\_COMPLIANT if SnapshotRetentionLimit for Redis cluster is less than the SnapshotRetentionPeriod parameter, i\.e from 0 to 15 as the default is 15\. 

**Identifier:** ELASTICACHE\_REDIS\_CLUSTER\_AUTOMATIC\_BACKUP\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

snapshotRetentionPeriod \(Optional\)Type: intDefault: 15  
Minimum snapshot retention period in days for Redis cluster\. Default is 15 days\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d149c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.