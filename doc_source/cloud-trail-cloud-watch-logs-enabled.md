# cloud\-trail\-cloud\-watch\-logs\-enabled<a name="cloud-trail-cloud-watch-logs-enabled"></a>

Checks whether AWS CloudTrail trails are configured to send logs to Amazon CloudWatch logs\. The trail is non\-compliant if the CloudWatchLogsLogGroupArn property of the trail is empty\. 

**Identifier:** CLOUD\_TRAIL\_CLOUD\_WATCH\_LOGS\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

expectedDeliveryWindowAge \(Optional\)Type: int  
Maximum age in hours of the most recent delivery to CloudWatch logs that satisfies compliance\.

## AWS CloudFormation template<a name="w29aac11c33c17b7c65c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.