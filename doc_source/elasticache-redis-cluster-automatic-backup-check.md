# elasticache\-redis\-cluster\-automatic\-backup\-check<a name="elasticache-redis-cluster-automatic-backup-check"></a>

Check if the Amazon ElastiCache Redis clusters have automatic backup turned on\. The rule is NON\_COMPLIANT if the SnapshotRetentionLimit for Redis cluster is less than the SnapshotRetentionPeriod parameter\. For example: If the parameter is 15 then the rule is non\-compliant if the snapshotRetentionPeriod is between 0\-15\. 

**Identifier:** ELASTICACHE\_REDIS\_CLUSTER\_AUTOMATIC\_BACKUP\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\) Region

**Parameters:**

snapshotRetentionPeriod \(Optional\)Type: intDefault: 15  
Minimum snapshot retention period in days for Redis cluster\. Default is 15 days\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d153c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.