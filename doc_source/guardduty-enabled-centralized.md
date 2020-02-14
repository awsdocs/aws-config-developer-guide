# guardduty\-enabled\-centralized<a name="guardduty-enabled-centralized"></a>

Checks whether Amazon GuardDuty is enabled in your AWS account and region\. If you provide an AWS account for centralization, the rule evaluates the Amazon GuardDuty results in the centralized account\. The rule is COMPLIANT when Amazon GuardDuty is enabled\.

**Identifier:** GUARDDUTY\_ENABLED\_CENTRALIZED

**Trigger type:** Configuration changes

**Parameters:**

 CentralMonitoringAccount \(optional\)  
Specify 12\-digit AWS Account for centralization of Amazon GuardDuty results\.

## AWS CloudFormation template<a name="w4aac13c29c17d167c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.