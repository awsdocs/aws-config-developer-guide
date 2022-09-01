# backup\-recovery\-point\-minimum\-retention\-check<a name="backup-recovery-point-minimum-retention-check"></a>

Checks if a recovery point expires no earlier than after the specified period\. The rule is NON\_COMPLIANT if the recovery point has a retention point that is less than the required retention period\. 

**Identifier:** BACKUP\_RECOVERY\_POINT\_MINIMUM\_RETENTION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

requiredRetentionDays \(Optional\)Type: intDefault: 35  
Required retention period in days\.

## AWS CloudFormation template<a name="w85aac12c32c17b9c59c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.