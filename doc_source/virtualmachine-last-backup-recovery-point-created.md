# virtualmachine\-last\-backup\-recovery\-point\-created<a name="virtualmachine-last-backup-recovery-point-created"></a>

Checks if a recovery point was created for AWS Backup\-Gateway VirtualMachines\. The rule is NON\_COMPLIANT if an AWS Backup\-Gateway VirtualMachines does not have a corresponding recovery point created within the specified time period\. 

**Identifier:** VIRTUALMACHINE\_LAST\_BACKUP\_RECOVERY\_POINT\_CREATED

**Resource Types:** AWS::BackupGateway::VirtualMachine

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

resourceTags \(Optional\)Type: String  
Tags of AWS Backup\-Gateway VirtualMachines for the rule to check, in JSON format `{"tagkey" : "tagValue"}`\.

resourceId \(Optional\)Type: String  
ID of AWS Backup\-Gateway VirtualMachine for the rule to check\.

recoveryPointAgeValue \(Optional\)Type: intDefault: 1  
Numerical value for maximum allowed age\. No more than 744 for hours, 31 for days\.

recoveryPointAgeUnit \(Optional\)Type: StringDefault: days  
Unit of time for maximum allowed age\. Accepted values: 'hours', 'days'\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d567c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.