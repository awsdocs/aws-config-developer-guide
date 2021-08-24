# backup\-plan\-min\-frequency\-and\-min\-retention\-check<a name="backup-plan-min-frequency-and-min-retention-check"></a>

Checks if a backup plan has a backup rule that satisfies the required frequency and retention period\. The rule is NON\_COMPLIANT if recovery points are not created at least as often as the specified frequency or expire before the specified period\. 

**Identifier:** BACKUP\_PLAN\_MIN\_FREQUENCY\_AND\_MIN\_RETENTION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Africa \(Cape Town\), Asia Pacific \(Osaka\), Europe \(Milan\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), US West \(Oregon\), and China \(Ningxia\) Region

**Parameters:**

requiredFrequencyValue \(Optional\)Type: intDefault: 1  
Numerical value for required backup frequency\. Maximum of 24 for hours, 31 for days\.

requiredRetentionDays \(Optional\)Type: intDefault: 35  
Required retention period in days\.

requiredFrequencyUnit \(Optional\)Type: StringDefault: days  
Unit of time for required backup frequency\. Accepted values: 'hours', 'days'\.

## AWS CloudFormation template<a name="w29aac11c33c17b7c37c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.