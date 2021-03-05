# guardduty\-enabled\-centralized<a name="guardduty-enabled-centralized"></a>

Checks whether GuardDuty is enabled\. You can optionally verify that the results are centralized in a specific AWS Account\. 

**Identifier:** GUARDDUTY\_ENABLED\_CENTRALIZED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), Europe \(Milan\), Middle East \(Bahrain\), Africa \(Cape Town\) Region

**Parameters:**

CentralMonitoringAccount \(Optional\)Type: String  
Comma separated list of AWS Accounts \(12\-digit\) where Amazon GuardDuty results are allowed to be centralized\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d193c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.