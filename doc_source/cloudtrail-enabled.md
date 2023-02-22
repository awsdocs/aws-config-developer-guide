# cloudtrail\-enabled<a name="cloudtrail-enabled"></a>

Checks if an AWS CloudTrail trail is enabled in your AWS account\. The rule is NON\_COMPLIANT if a trail is not enabled\. You can specify for the rule to check a specific S3 bucket, SNS topic, and Amazon CloudWatch log group\.

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

## AWS CloudFormation template<a name="w2aac12c33c15b9d113c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.