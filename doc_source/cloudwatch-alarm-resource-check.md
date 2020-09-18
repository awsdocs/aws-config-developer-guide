# cloudwatch\-alarm\-resource\-check<a name="cloudwatch-alarm-resource-check"></a>

Checks whether the specified resource type has a CloudWatch alarm for the specified metric\. For resource type, you can specify EBS volumes, EC2 instances, RDS clusters, or S3 buckets\.

**Identifier:**CLOUDWATCH\_ALARM\_RESOURCE\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions

**Parameters:**

resourceType  
AWS resource type\. The value can be one of the following:  
+ AWS::EC2::Volume
+ AWS::EC2::Instance
+ AWS::S3::Bucket

metricName  
The name of the metric associated with the alarm \(for example, "CPUUtilization" for EC2 instances\)\.

## AWS CloudFormation template<a name="w22aac11c29c17c65c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.