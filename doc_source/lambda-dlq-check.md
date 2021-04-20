# lambda\-dlq\-check<a name="lambda-dlq-check"></a>

Checks whether an AWS Lambda function is configured with a dead\-letter queue\. The rule is NON\_COMPLIANT if the Lambda function is not configured with a dead\-letter queue\. 

**Identifier:** LAMBDA\_DLQ\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Ningxia\), Asia Pacific \(Osaka\) Region

**Parameters:**

dlqArns \(Optional\)Type: String  
Comma\-separated list of Amazon SQS and Amazon SNS ARNs that must be configured as the Lambda function dead\-letter queue target\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d241c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.