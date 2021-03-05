# dynamodb\-throughput\-limit\-check<a name="dynamodb-throughput-limit-check"></a>

Checks whether provisioned DynamoDB throughput is approaching the maximum limit for your account\. 

**Identifier:** DYNAMODB\_THROUGHPUT\_LIMIT\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

accountRCUThresholdPercentage \(Optional\)Type: intDefault: 80  
Percentage of provisioned read capacity units for your account\. When this value is reached, the rule is marked as noncompliant\.

accountWCUThresholdPercentage \(Optional\)Type: intDefault: 80  
Percentage of provisioned write capacity units for your account\. When this value is reached, the rule is marked as noncompliant\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d103c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.