# cloudtrail\-enabled<a name="cloudtrail-enabled"></a>

Checks if AWS CloudTrail is enabled in your AWS account\. Optionally, you can specify which S3 bucket, SNS topic, and AWS CloudTrail ARN to use\. The rule is NON\_COMPLIANT if AWS CloudTrail is not enabled\.

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

## AWS CloudFormation template<a name="w79aac11c32c17b9d107c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.