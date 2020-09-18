# lambda\-dlq\-check<a name="lambda-dlq-check"></a>

Checks whether an AWS Lambda function is configured with a dead\-letter queue\. The rule is NON\_COMPLIANT if the Lambda function is not configured with a dead\-letter queue\.

**Identifier:** LAMBDA\_DLQ\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except China \(Ningxia\)

**Parameters:**

 dlqArns  
\(Optional\) Comma\-separated list of Amazon SQS and Amazon SNS ARNs that must be configured as the Lambda function dead\-letter queue target\.

## AWS CloudFormation template<a name="w22aac11c29c17d225c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.