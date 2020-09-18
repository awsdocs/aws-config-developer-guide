# wafv2\-logging\-enabled<a name="wafv2-logging-enabled"></a>

Checks whether logging is enabled on AWS Web Application Firewall \(WAFV2\) regional and global web access control list \(ACLs\)\. The rule is NON\_COMPLIANT if the logging is enabled but the logging destination does not match the value of the parameter\. 

**Identifier:** WAFV2\_LOGGING\_ENABLED

**Trigger type:** Periodic

**AWS Region:**All supported AWS Regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Milan\), Africa \(Cape Town\) Regions

**Parameters:**

KinesisFirehoseDeliveryStreamArns \(Optional\)Type: CSV  
Comma separated list of Kinesis Firehose delivery stream ARNs\.

## AWS CloudFormation template<a name="w22aac11c29c17d335c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.