# lambda\-function\-settings\-check<a name="lambda-function-settings-check"></a>

Checks if the AWS Lambda function settings for runtime, role, timeout, and memory size match the expected values\. The rule ignores functions with the 'Image' package type\. The rule is NON\_COMPLIANT if the Lambda function settings do not match the expected values\.

**Identifier:** LAMBDA\_FUNCTION\_SETTINGS\_CHECK

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

runtimeType: CSV  
Comma\-separated list of AWS Lambda runtime values

role \(Optional\)Type: String  
Name or ARN of the AWS Lambda execution role

timeout \(Optional\)Type: intDefault: 3  
AWS Lambda function timeout in seconds

memorySize \(Optional\)Type: intDefault: 128  
AWS Lambda function size in megabytes

## Proactive Evaluation<a name="w2aac12c33c15b9d377c17"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive)\. For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
    "MemorySize": Integer*,
    "Role": String*,
    "Runtime": String*,
    "Timeout": Integer*
} 
...
```

\*For more information on valid values for these inputs, see [MemorySize](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-memorysize), [Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-role), [Runtime](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-runtime), and [Timeout](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-timeout) in the AWS CloudFormation User Guide\.

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html)\. 

## AWS CloudFormation template<a name="w2aac12c33c15b9d377c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.