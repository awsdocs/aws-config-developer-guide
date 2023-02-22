# guardduty\-non\-archived\-findings<a name="guardduty-non-archived-findings"></a>

Checks whether Amazon GuardDuty has findings that are non archived\. The rule is NON\_COMPLIANT if Amazon GuardDuty has non archived low/medium/high severity findings older than the specified number in the daysLowSev/daysMediumSev/`daysHighSev` parameter\. 

**Identifier:** GUARDDUTY\_NON\_ARCHIVED\_FINDINGS

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East \(Bahrain\), China \(Beijing\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), AWS GovCloud \(US\-East\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

daysLowSev \(Optional\)Type: intDefault: 30  
The number of days Amazon GuardDuty low severity findings are allowed to stay non archived\. The default is 30 days\.

daysMediumSev \(Optional\)Type: intDefault: 7  
The number of days Amazon GuardDuty medium severity findings are allowed to stay non archived\. The default is 7 days\.

daysHighSev \(Optional\)Type: intDefault: 1  
The number of days Amazon GuardDuty high severity findings are allowed to stay non archived\. The default is 1 day\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d329c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.