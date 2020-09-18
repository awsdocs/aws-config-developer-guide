# dynamodb\-autoscaling\-enabled<a name="dynamodb-autoscaling-enabled"></a>

Checks whether Auto Scaling or On\-Demand is enabled on your DynamoDB tables and/or global secondary indexes\. Optionally you can set the read and write capacity units for the table or global secondary index\.

**Identifier:** DYNAMODB\_AUTOSCALING\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions except AWS GovCloud \(US\-East\) and AWS GovCloud \(US\-West\)

**Parameters:**

minProvisionedReadCapacity  
The minimum number of units that should be provisioned with read capacity in the Auto Scaling group\.

minProvisionedWriteCapacity  
The minimum number of units that should be provisioned with write capacity in the Auto Scaling group\.

maxProvisionedReadCapacity  
The maximum number of units that should be provisioned with read capacity in the Auto Scaling group\.

maxProvisionedWriteCapacity  
The maximum number of units that should be provisioned with write capacity in the Auto Scaling group\.

targetReadUtilization  
The target utilization percentage for read capacity\. Target utilization is expressed in terms of the ratio of consumed capacity to provisioned capacity\.

targetWriteUtilization  
The target utilization percentage for write capacity\. Target utilization is expressed in terms of the ratio of consumed capacity to provisioned capacity\.

## AWS CloudFormation template<a name="w22aac11c29c17c93c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.