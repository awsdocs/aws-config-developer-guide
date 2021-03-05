# dynamodb\-autoscaling\-enabled<a name="dynamodb-autoscaling-enabled"></a>

This rule checks whether Auto Scaling is enabled on your DynamoDB tables\. Optionally you can set the read and write capacity units for the table\. 

**Identifier:** DYNAMODB\_AUTOSCALING\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\) Region

**Parameters:**

minProvisionedReadCapacity \(Optional\)Type: int  
Minimum provisioned capacity\.

maxProvisionedReadCapacity \(Optional\)Type: int  
Maximum provisioned capacity\.

targetReadUtilization \(Optional\)Type: double  
Target utilization of read capacity

minProvisionedWriteCapacity \(Optional\)Type: int  
Minimum provisioned capacity\.

maxProvisionedWriteCapacity \(Optional\)Type: int  
Maximum provisioned capacity\.

targetWriteUtilization \(Optional\)Type: double  
Target utilization of write capacity

## AWS CloudFormation template<a name="w24aac11c29c17b7c93c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.