# dynamodb\-throughput\-limit\-check<a name="dynamodb-throughput-limit-check"></a>

Checks whether provisioned DynamoDB throughput is approaching the maximum limit for your account\. By default, the rule checks if provisioned throughput exceeds a threshold of 80% of your account limits\.

**Identifier:** DYNAMODB\_THROUGHPUT\_LIMIT\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

accountRCUThresholdPercentage  
 Percentage of provisioned read capacity units for your account\. When this value is reached, the rule is marked as NON\_COMPLIANT\. 

accountWCUThresholdPercentage  
 Percentage of provisioned write capacity units for your account\. When this value is reached, the rule is marked as NON\_COMPLIANT\. 

## AWS CloudFormation template<a name="w22aac11c29c17d103c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.