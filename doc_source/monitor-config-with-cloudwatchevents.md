# Monitoring AWS Config with Amazon CloudWatch Events<a name="monitor-config-with-cloudwatchevents"></a>

Amazon CloudWatch Events delivers a near real\-time stream of system events that describe changes in AWS resources\. Use Amazon CloudWatch Events to detect and react to changes in the status of AWS Config events\.

You can create a rule that runs whenever there is a state transition, or when there is a transition to one or more states that are of interest\. Then, based on rules you create, Amazon CloudWatch Events invokes one or more target actions when an event matches the values you specify in a rule\. Depending on the type of event, you might want to send notifications, capture event information, take corrective action, initiate events, or take other actions\. 

Before you create event rules for AWS Config, however, you should do the following: 
+ Familiarize yourself with events, rules, and targets in CloudWatch Events\. For more information, see [What Is Amazon CloudWatch Events?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)
+ For more information about how to get started with CloudWatch Events and set up rules, see [Getting Started with CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CWE_GettingStarted.html)\.
+ Create the target or targets you will use in your event rules\.

**Topics**
+ [Amazon CloudWatch Events format for AWS Config](#cloudwatch-event-format-for-awsconfig)
+ [Creating Amazon CloudWatch Events Rule for AWS Config](#create-cloudwatch-events-rule-for-awsconfig)

## Amazon CloudWatch Events format for AWS Config<a name="cloudwatch-event-format-for-awsconfig"></a>

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

## Creating Amazon CloudWatch Events Rule for AWS Config<a name="create-cloudwatch-events-rule-for-awsconfig"></a>

Use the following steps to create a CloudWatch Events rule that triggers on an event emitted by AWS Config\.

1. Open the CloudWatch console at [https://console\.aws\.amazon\.com/cloudwatch/]()\.

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