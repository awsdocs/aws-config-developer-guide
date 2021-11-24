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
+ [Monitoring AWS Resource Changes with Amazon SQS](#monitor-resource-changes)
+ [Monitoring AWS Config with Amazon CloudWatch Events](#monitor-config-with-cloudwatchevents)

## Monitoring AWS Resource Changes with Amazon SQS<a name="monitor-resource-changes"></a>

AWS Config uses Amazon Simple Notification Service \(SNS\) to send you notifications every time a supported AWS resource is created, updated, or otherwise modified as a result of user API activity\. However, you might be interested in only certain resource configuration changes\. For example, you might consider it critical to know when someone modifies the configuration of a security group, but not need to know every time there is a change to tags on your Amazon EC2 instances\. Or, you might want to write a program that performs specific actions when specific resources are updated\. For example, you might want to start a certain workflow when a security group configuration is changed\. If you want to programmatically consume the data from AWS Config in these or other ways, use an Amazon Simple Queue Service queue as the notification endpoint for Amazon SNS\.

**Note**  
Notifications can also come from Amazon SNS in the form of an email, a Short Message Service \(SMS\) message to SMS\-enabled mobile phones and smartphones, a notification message to an application on a mobile device, or a notification message to one or more HTTP or HTTPS endpoints\.

You can have a single SQS queue subscribe to multiple topics, whether you have one topic per region or one topic per account per region\. You must subscribe the queue to your desired SNS topic\. \(You can subscribe multiple queues to one SNS topic\.\) For more information, see [Sending Amazon SNS Messages to Amazon SQS Queues](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToSQS.html)\.

### Permissions for Amazon SQS<a name="sqs-policy"></a>

To use Amazon SQS with AWS Config, you must configure a policy that grants permissions to your account to perform all actions that are allowed on an SQS queue\. The following example policy grants the account number 111122223333 and account number 444455556666 permission to send messages pertaining to each configuration change to the queue named arn:aws:sqs:us\-east\-2:444455556666:queue1\.

```
{
  "Version": "2012-10-17",
  "Id": "Queue1_Policy_UUID",
  "Statement": 
    {
       "Sid":"Queue1_SendMessage",
       "Effect": "Allow",
       "Principal": {
            "AWS": ["111122223333","444455556666"]
         },
        "Action": "sqs:SendMessage",
        "Resource": "arn:aws:sqs:us-east-2:444455556666:queue1"
     }
}
```

You must also create a policy that grants permissions for connections between an SNS topic and the SQS queue that subscribes to that topic\. The following is an example policy that permits the SNS topic with the Amazon Resource Name \(ARN\) arn:aws:sns:us\-east\-2:111122223333:test\-topic to perform any actions on the queue named arn:aws:sqs:us\-east\-2:111122223333:test\-topic\-queue\. 

**Note**  
The account for the SNS topic and the SQS queue must be in the same region\.

```
{
  "Version": "2012-10-17",
  "Id": "SNStoSQS",
  "Statement": 
    {
      "Sid":"rule1",
      "Effect": "Allow",
      "Principal": {
        "Service": "sns.amazonaws.com"
      },
      "Action": "SQS:SendMessage",
      "Resource": "arn:aws:sqs:us-east-2:111122223333:test-topic-queue",
      "Condition" : {
        "StringEquals" : {
          "aws:SourceArn":"arn:aws:sns:us-east-2:111122223333:test-topic"
        }
      }
    }
}
```

Each policy can include statements that cover only a single queue, not multiple queues\. For information about other restrictions on Amazon SQS policies, see [Special Information for Amazon SQS Policies](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AccessPolicyLanguage_SpecialInfo.html)\.

## Monitoring AWS Config with Amazon CloudWatch Events<a name="monitor-config-with-cloudwatchevents"></a>

**Note**  
Amazon EventBridge is the preferred way to manage your events\. CloudWatch Events and EventBridge are the same underlying service and API, but EventBridge provides more features\. Changes you make in either CloudWatch or EventBridge will appear in each console\. For more informance, see [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/index.html)\. 

Amazon CloudWatch Events delivers a near real\-time stream of system events that describe changes in AWS resources\. Use Amazon CloudWatch Events to detect and react to changes in the status of AWS Config events\.

You can create a rule that runs whenever there is a state transition, or when there is a transition to one or more states that are of interest\. Then, based on rules you create, Amazon CloudWatch Events invokes one or more target actions when an event matches the values you specify in a rule\. Depending on the type of event, you might want to send notifications, capture event information, take corrective action, initiate events, or take other actions\. 

Before you create event rules for AWS Config, however, you should do the following: 
+ Familiarize yourself with events, rules, and targets in CloudWatch Events\. For more information, see [What Is Amazon CloudWatch Events?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)
+ For more information about how to get started with CloudWatch Events and set up rules, see [Getting Started with CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CWE_GettingStarted.html)\.
+ Create the target or targets you will use in your event rules\.

**Topics**
+ [Amazon CloudWatch Events format for AWS Config](#cloudwatch-event-format-for-awsconfig)
+ [Creating Amazon CloudWatch Events Rule for AWS Config](#create-cloudwatch-events-rule-for-awsconfig)

### Amazon CloudWatch Events format for AWS Config<a name="cloudwatch-event-format-for-awsconfig"></a>

The CloudWatch [event](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html) for AWS Config has the following format:

```
          {
             "version": "0",
             "id": "cd4d811e-ab12-322b-8255-872ce65b1bc8",
             "detail-type": "event type",
             "source": "aws.config",
             "account": "111122223333",
             "time": "2018-03-22T00:38:11Z",
             "region": "us-east-1",
             "resources": [resources],
             "detail": {specific message type}
          }
```

### Creating Amazon CloudWatch Events Rule for AWS Config<a name="create-cloudwatch-events-rule-for-awsconfig"></a>

Use the following steps to create a CloudWatch Events rule that triggers on an event emitted by AWS Config\. Events are emitted on a best effort basis\.

1. Open the CloudWatch console at [https://console\.aws\.amazon\.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/)\.

1. In the navigation pane, choose **Events**\.

1. Choose **Create rule**\.

1. On the **Step 1: Create rule** page, for **Service Name**, choose **Config**\.

1. For **Event Type**, choose the event type that triggers the rule:
   + Choose **All Events** to make a rule that applies to all AWS services\. If you choose this option, you cannot choose specific message types, rule names, resource types, or resource IDs\.
   + Choose **AWS API Call via CloudTrail** to base rules on API calls made to this service\. For more information about creating this type of rule, see [Creating a CloudWatch Events Rule That Is Triggered on an AWS API Call Using AWS CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-CloudTrail-Rule.html)\.
   + Choose **Config Configuration Item Change** to get notifications when a resource in your account changes\.
   + Choose **Config Rules Compliance Change** to get notifications when a compliance check to your rules fails\.
   + Choose **Config Rules Re\-evaluation Status** to get reevaluation status notifications\. 
   + Choose **Config Configuration Snapshot Delivery Status** to get configuration snapshot delivery status notifications\.
   + Choose **Config Configuration History Delivery Status** to get configuration history delivery status notifications\.

1. Choose **Any message type** to receive notifications of any type\. Choose **Specific message type\(s\)** to receive the following types of notifications:
   + If you choose **ConfigurationItemChangeNotification**, you receive messages when AWS Config successfully delivers the configuration snapshot to your Amazon S3 bucket\.
   + If you choose **ComplianceChangeNotification**, you receive messages when the compliance type of a resource that AWS Config evaluates has changed\.
   + If you choose **ConfigRulesEvaluationStarted**, you receive messages when AWS Config starts evaluating your rule against the specified resources\.
   + If you choose **ConfigurationSnapshotDeliveryCompleted**, you receive messages when AWS Config successfully delivers the configuration snapshot to your Amazon S3 bucket\.
   + If you choose **ConfigurationSnapshotDeliveryFailed**, you receive messages when AWS Config fails to deliver the configuration snapshot to your Amazon S3 bucket\.
   + If you choose **ConfigurationSnapshotDeliveryStarted**, you receive messages when AWS Config starts delivering the configuration snapshot to your Amazon S3 bucket\.
   + If you choose **ConfigurationHistoryDeliveryCompleted**, you receive messages when AWS Config successfully delivers the configuration history to your Amazon S3 bucket\.

1. If you chose a specific event type from the **Event Type** drop\-down list, choose **Any resource type** to make a rule that applies to all AWS Config supported resource types\.

   Or choose **Specific resource type\(s\)**, and then type the AWS Config supported resource type \(for example, `AWS::EC2::Instance`\)\.

1. If you chose a specific event type from the **Event Type** drop\-down list, choose **Any resource ID** to include any AWS Config supported resource ID\.

   Or choose **Specific resource ID\(s\)**, and then type the AWS Config supported resource ID \(for example, `i-04606de676e635647`\)\.

1. If you chose a specific event type from the **Event Type** drop\-down list, choose **Any rule name** to include any AWS Config supported rule\.

   Or choose **Specific rule name\(s\)**, and then type the AWS Config supported rule \(for example, **required\-tags**\)\.

1. Review your rule setup to make sure it meets your event\-monitoring requirements\.

1. In the **Targets** area, choose Add target\*\.

1. In the **Select target type** list, choose the type of target you have prepared to use with this rule, and then configure any additional options required by that type\.

1. Choose **Configure details**\.

1. On the **Configure rule details** page, type a name and description for the rule, and then choose the **State** box to enable the rule as soon as it is created\.

1. Choose **Create rule** to confirm your selection\.