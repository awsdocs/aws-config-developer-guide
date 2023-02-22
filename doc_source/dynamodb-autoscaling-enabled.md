# dynamodb\-autoscaling\-enabled<a name="dynamodb-autoscaling-enabled"></a>

Checks if Auto Scaling or On\-Demand is enabled on your DynamoDB tables and/or global secondary indexes\. Optionally you can set the read and write capacity units for the table or global secondary index\.

**Identifier:** DYNAMODB\_AUTOSCALING\_ENABLED

**Resource Types:** AWS::DynamoDB::Table

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

minProvisionedReadCapacity \(Optional\)Type: int  
The minimum number of units that should be provisioned with read capacity in the Auto Scaling group\.

maxProvisionedReadCapacity \(Optional\)Type: int  
The maximum number of units that should be provisioned with read capacity in the Auto Scaling group\.

targetReadUtilization \(Optional\)Type: double  
The target utilization percentage for read capacity\. Target utilization is expressed in terms of the ratio of consumed capacity to provisioned capacity\.

minProvisionedWriteCapacity \(Optional\)Type: int  
The minimum number of units that should be provisioned with write capacity in the Auto Scaling group\.

maxProvisionedWriteCapacity \(Optional\)Type: int  
The maximum number of units that should be provisioned with write capacity in the Auto Scaling group\.

targetWriteUtilization \(Optional\)Type: double  
The target utilization percentage for write capacity\. Target utilization is expressed in terms of the ratio of consumed capacity to provisioned capacity\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d155c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.