# Logging and Monitoring in AWS Config<a name="security-logging-and-monitoring"></a>

AWS Config is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Config\. Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Config and your AWS solutions\.

## Logging AWS Config API Calls with AWS CloudTrail<a name="log-api-calls"></a>

CloudTrail captures all API calls for AWS Config as events\. The calls captured include calls from the AWS Config console and code calls to the AWS Config API operations\. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Config\. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**\. Using the information collected by CloudTrail, you can determine the request that was made to AWS Config, the IP address from which the request was made, who made the request, when it was made, and additional details\. 

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/)\.

**Topics**
+ [AWS Config Information in CloudTrail](#service-name-info-in-cloudtrail)
+ [Understanding AWS Config Log File Entries](#understanding-awsconfig-entries)
+ [Example Log Files](cloudtrail-log-files-for-aws-config.md)

### AWS Config Information in CloudTrail<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account\. When activity occurs in AWS Config, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**\. You can view, search, and download recent events in your AWS account\. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)\. 

For an ongoing record of events in your AWS account, including events for AWS Config, create a trail\. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket\. By default, when you create a trail in the console, the trail applies to all AWS Regions\. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify\. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs\. For more information, see the following: 
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All AWS Config operations are logged by CloudTrail and are documented in the [AWS Config API Reference](https://docs.aws.amazon.com/config/latest/APIReference/)\. For example, calls to the [DeliverConfigSnapshot](https://docs.aws.amazon.com/config/latest/APIReference/API_DeliverConfigSnapshot.html), [DeleteDeliveryChannel](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteDeliveryChannel.html), and [DescribeDeliveryChannels](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeDeliveryChannels.html) operations generate entries in the CloudTrail log files\. 

Every event or log entry contains information about who generated the request\. The identity information helps you determine the following: 
+ Whether the request was made with root or AWS Identity and Access Management \(IAM\) user credentials\.
+ Whether the request was made with temporary security credentials for a role or federated user\.
+ Whether the request was made by another AWS service\.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html)\.

### Understanding AWS Config Log File Entries<a name="understanding-awsconfig-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify\. CloudTrail log files contain one or more log entries\. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on\. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order\. 

## Monitoring<a name="monitoring"></a>

You can use other AWS services to monitor AWS Config resources\.
+ You can use Amazon Simple Notification Service \(SNS\) to send you notifications every time a supported AWS resource is created, updated, or otherwise modified as a result of user API activity\.
+ You can use Amazon CloudWatch Events to detect and react to changes in the status of AWS Config events\.

**Topics**
+ [Logging AWS Config API Calls with AWS CloudTrail](#log-api-calls)
+ [Monitoring](#monitoring)
+ [Monitoring AWS Resource Changes with Amazon SQS](monitor-resource-changes.md)
+ [Monitoring AWS Config with Amazon CloudWatch Events](monitor-config-with-cloudwatchevents.md)