# lambda\-inside\-vpc<a name="lambda-inside-vpc"></a>

Checks whether an AWS Lambda function is in an Amazon Virtual Private Cloud\. The rule is NON\_COMPLIANT if the Lambda function is not in a VPC\. 

**Identifier:** LAMBDA\_INSIDE\_VPC

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except China \(Ningxia\)

**Parameters:**

 subnetIds  
\(Optional\) Comma\-separated list of subnet IDs that Lambda functions must be associated with\.

## AWS CloudFormation template<a name="w22aac11c29c17d231c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.