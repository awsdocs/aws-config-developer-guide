# lambda\-function\-settings\-check<a name="lambda-function-settings-check"></a>

Checks that the AWS Lambda function settings for runtime, role, timeout, and memory size match the expected values\. 

**Identifier:** LAMBDA\_FUNCTION\_SETTINGS\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Ningxia\) Region

**Parameters:**

runtimeType: CSV  
Comma\-separated list of AWS Lambda runtime values

role \(Optional\)Type: String  
Name or ARN of the AWS Lambda execution role

timeout \(Optional\)Type: intDefault: 3  
AWS Lambda function timeout in seconds

memorySize \(Optional\)Type: intDefault: 128  
AWS Lambda function size in megabytes

## AWS CloudFormation template<a name="w26aac11c31c17b7d239c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.