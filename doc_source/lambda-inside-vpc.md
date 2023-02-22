# lambda\-inside\-vpc<a name="lambda-inside-vpc"></a>

Checks whether an AWS Lambda function is allowed access to an Amazon Virtual Private Cloud\. The rule is NON\_COMPLIANT if the Lambda function is not VPC enabled\. 

**Identifier:** LAMBDA\_INSIDE\_VPC

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

subnetIds \(Optional\)Type: String  
Comma\-separated list of Subnet IDs that Lambda functions can be associated with\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d379c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.