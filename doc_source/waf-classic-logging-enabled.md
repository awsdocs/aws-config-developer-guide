# waf\-classic\-logging\-enabled<a name="waf-classic-logging-enabled"></a>

Checks if logging is enabled on AWS Web Application Firewall \(WAF\) classic global web ACLs\. This rule is NON\_COMPLIANT for a global web ACL, if it does not have logging enabled\. 

**Identifier:** WAF\_CLASSIC\_LOGGING\_ENABLED

**Trigger type:** Periodic

**AWS Region:**Only available in US East \(N\. Virginia\) Region

**Parameters:**

KinesisFirehoseDeliveryStreamArns \(Optional\)Type: CSV  
Comma separated list of Amazon Kinesis stream ARN for AWS WAF logs\.

## AWS CloudFormation template<a name="w22aac11c29c17d333c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.