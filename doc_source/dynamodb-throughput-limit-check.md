# dynamodb\-throughput\-limit\-check<a name="dynamodb-throughput-limit-check"></a>

Checks if provisioned DynamoDB throughput is approaching the maximum limit for your account\. By default, the rule checks if provisioned throughput exceeds a threshold of 80 percent of your account limits\.

**Identifier:** DYNAMODB\_THROUGHPUT\_LIMIT\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

accountRCUThresholdPercentage \(Optional\)Type: intDefault: 80  
Percentage of provisioned read capacity units for your account\. When this value is reached, the rule is marked as noncompliant\.

accountWCUThresholdPercentage \(Optional\)Type: intDefault: 80  
Percentage of provisioned write capacity units for your account\. When this value is reached, the rule is marked as noncompliant\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d179c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.