# guardduty\-non\-archived\-findings<a name="guardduty-non-archived-findings"></a>

Checks whether the Amazon GuardDuty has findings that are non archived\. The rule is NON\_COMPLIANT if Amazon GuardDuty has non archived low/medium/high severity findings older than the specified number in the daysLowSev/daysMediumSev/daysHighSev parameter\.

**Identifier:** GUARDDUTY\_NON\_ARCHIVED\_FINDINGS

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\) and China \(Ningxia\) 

**Parameters:**

daysLowSev  
The number of days Amazon GuardDuty low severity findings are allowed to stay non archived\. The default is 30 days\.

daysMediumSev  
The number of days the Amazon GuardDuty medium severity findings are allowed to stay non archived\. The default is 7 days\.

daysHighSev  
The number of days Amazon GuardDuty high severity findings are allowed to stay non archived\. The default is 1 day\.

## AWS CloudFormation template<a name="w4aac13c29c17d169c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.