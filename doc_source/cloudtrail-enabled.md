# cloudtrail\-enabled<a name="cloudtrail-enabled"></a>

Checks whether AWS CloudTrail is enabled in your AWS account\. Optionally, you can specify which S3 bucket, SNS topic, and Amazon CloudWatch Logs ARN to use\.

**Identifier:** CLOUD\_TRAIL\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions

**Parameters:**

 s3BucketName   
 The name of the S3 bucket for AWS CloudTrail to deliver log files to\. 

 snsTopicArn   
 The ARN of the SNS topic for AWS CloudTrail to use for notifications\. 

 cloudWatchLogsLogGroupArn   
 The ARN of the Amazon CloudWatch log group for AWS CloudTrail to send data to\. 

## AWS CloudFormation template<a name="w22aac11c29c17c53c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.