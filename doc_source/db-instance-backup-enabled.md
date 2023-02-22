# db\-instance\-backup\-enabled<a name="db-instance-backup-enabled"></a>

Checks if RDS DB instances have backups enabled\. Optionally, the rule checks the backup retention period and the backup window\.

**Identifier:** DB\_INSTANCE\_BACKUP\_ENABLED

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

backupRetentionPeriod \(Optional\)Type: int  
Retention period for backups\.

backupRetentionMinimum \(Optional\)Type: int  
Minimum retention period for backups\.

preferredBackupWindow \(Optional\)Type: String  
Time range in which backups are created\.

checkReadReplicas \(Optional\)Type: boolean  
Checks whether RDS DB instances have backups enabled for read replicas\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d147c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.