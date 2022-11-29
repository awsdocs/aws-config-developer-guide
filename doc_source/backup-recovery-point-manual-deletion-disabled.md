# backup\-recovery\-point\-manual\-deletion\-disabled<a name="backup-recovery-point-manual-deletion-disabled"></a>

Checks if a backup vault has an attached resource\-based policy which prevents deletion of recovery points\. The rule is NON\_COMPLIANT if the Backup Vault does not have resource\-based policies or has policies without a suitable 'Deny' statement \(statement with backup:DeleteRecoveryPoint, backup:UpdateRecoveryPointLifecycle, and backup:PutBackupVaultAccessPolicy permissions\)\. 

**Identifier:** BACKUP\_RECOVERY\_POINT\_MANUAL\_DELETION\_DISABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

principalArnList \(Optional\)Type: CSV  
Comma\-separated list of AWS Identity and Access Management \(IAM\) Amazon Resource Names \(ARNs\) for the rule to NOT check\.

## AWS CloudFormation template<a name="w2aac12c31c27b9c57c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.