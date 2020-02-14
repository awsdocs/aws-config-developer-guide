# multi\-region\-cloud\-trail\-enabled<a name="multi-region-cloud-trail-enabled"></a>

Checks that there is at least one multi\-region AWS CloudTrail\. The rule is NON\_COMPLIANT if the trails do not match inputs parameters\.

**Identifier:** MULTI\_REGION\_CLOUD\_TRAIL\_ENABLED

**Trigger type:** Periodic

**Parameters \(optional\):**

 s3BucketName  
Name of Amazon S3 bucket for AWS CloudTrail to deliver log files to\.

 snsTopicArn  
Amazon SNS topic ARN for AWS CloudTrail to use for notifications\.

cloudWatchLogsLogGroupArn  
Amazon CloudWatch log group ARN for AWS CloudTrail to send data to\.

includeManagementEvents  
Event selector to include management events for the AWS CloudTrail\.

readWriteType  
Type of events to record\. Valid values are `ReadOnly`, `WriteOnly` and `ALL`\.

## AWS CloudFormation template<a name="w4aac13c29c17d209c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.