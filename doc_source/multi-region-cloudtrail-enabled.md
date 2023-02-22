# multi\-region\-cloudtrail\-enabled<a name="multi-region-cloudtrail-enabled"></a>

Checks if there is at least one multi\-region AWS CloudTrail\. The rule is NON\_COMPLIANT if the trails do not match input parameters\. The rule is NON\_COMPLIANT if the `ExcludeManagementEventSources` field is not empty or if AWS CloudTrail is configured to exclude management events such as AWS KMS events or Amazon RDS Data API events\.

**Identifier:** MULTI\_REGION\_CLOUD\_TRAIL\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East \(UAE\) Region

**Parameters:**

s3BucketName \(Optional\)Type: String  
Name of Amazon S3 bucket for AWS CloudTrail to deliver log files to\.

snsTopicArn \(Optional\)Type: String  
Amazon SNS topic ARN for AWS CloudTrail to use for notifications\.

cloudWatchLogsLogGroupArn \(Optional\)Type: String  
Amazon CloudWatch log group ARN for AWS CloudTrail to send data to\.

includeManagementEvents \(Optional\)Type: boolean  
Event selector to include management events for the AWS CloudTrail\.

readWriteType \(Optional\)Type: String  
Type of events to record\. Valid values are ReadOnly, WriteOnly and ALL\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d385c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.