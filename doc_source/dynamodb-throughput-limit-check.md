# dynamodb\-throughput\-limit\-check<a name="dynamodb-throughput-limit-check"></a>

Checks if provisioned DynamoDB throughput is approaching the maximum limit for your account\. By default, the rule checks if provisioned throughput exceeds a threshold of 80 percent of your account limits\.

**Identifier:** DYNAMODB\_THROUGHPUT\_LIMIT\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

accountRCUThresholdPercentage \(Optional\)Type: intDefault: 80  
Percentage of provisioned read capacity units for your account\. When this value is reached, the rule is marked as NON\_COMPLIANT\.

accountWCUThresholdPercentage \(Optional\)Type: intDefault: 80  
Percentage of provisioned write capacity units for your account\. When this value is reached, the rule is marked as NON\_COMPLIANT\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d109c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.