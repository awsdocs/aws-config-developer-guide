# lambda\-concurrency\-check<a name="lambda-concurrency-check"></a>

Checks whether the AWS Lambda function is configured with function\-level concurrent execution limit\. The rule is NON\_COMPLIANT if the Lambda function is not configured with function\-level concurrent execution limit\. 

**Identifier:** LAMBDA\_CONCURRENCY\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Ningxia\), Asia Pacific \(Osaka\) Region

**Parameters:**

ConcurrencyLimitLow \(Optional\)Type: String  
Minimum concurrency execution limit

ConcurrencyLimitHigh \(Optional\)Type: String  
Maximum concurrency execution limit

## AWS CloudFormation template<a name="w29aac11c33c17b7d243c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.