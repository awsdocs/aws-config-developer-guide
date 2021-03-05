# cloudtrail\-enabled<a name="cloudtrail-enabled"></a>

Checks whether AWS CloudTrail is enabled in your AWS account\. 

**Identifier:** CLOUD\_TRAIL\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

s3BucketName \(Optional\)Type: String  
Name of S3 bucket for CloudTrail to deliver log files to\.

snsTopicArn \(Optional\)Type: String  
SNS topic ARN for CloudTrail to use for notifications\.

cloudWatchLogsLogGroupArn \(Optional\)Type: String  
CloudWatch log group ARN for CloudTrail to send data to\.

## AWS CloudFormation template<a name="w24aac11c29c17b7c65c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.