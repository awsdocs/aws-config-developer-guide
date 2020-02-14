# db\-instance\-backup\-enabled<a name="db-instance-backup-enabled"></a>

Checks whether RDS DB instances have backups enabled\. Optionally, the rule checks the backup retention period and the backup window\.

**Identifier:** DB\_INSTANCE\_BACKUP\_ENABLED

**Trigger type:** Configuration changes

**Parameters:**

 backupRetentionPeriod   
 Retention period for backups\. 

 preferredBackupWindow   
 Time range in which backups are created\. 

 checkReadReplicas   
 Checks whether RDS DB instances have backups enabled for read replicas\. 

## AWS CloudFormation template<a name="w4aac13c29c17c85c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.