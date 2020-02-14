# dynamodb\-throughput\-limit\-check<a name="dynamodb-throughput-limit-check"></a>

Checks whether provisioned DynamoDB throughput is approaching the maximum limit for your account\. By default, the rule checks if provisioned throughput exceeds a threshold of 80% of your account limits\.

**Identifier:** DYNAMODB\_THROUGHPUT\_LIMIT\_CHECK

**Trigger type:** Periodic

**Parameters:**

accountRCUThresholdPercentage  
 Percentage of provisioned read capacity units for your account\. When this value is reached, the rule is marked as NON\_COMPLIANT\. 

accountWCUThresholdPercentage  
 Percentage of provisioned write capacity units for your account\. When this value is reached, the rule is marked as NON\_COMPLIANT\. 

## AWS CloudFormation template<a name="w4aac13c29c17c97c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.