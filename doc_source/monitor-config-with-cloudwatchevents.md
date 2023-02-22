# Monitoring AWS Config with Amazon EventBridge<a name="monitor-config-with-cloudwatchevents"></a>

Amazon EventBridge delivers a near real\-time stream of system events that describe changes in AWS resources\. Use Amazon EventBridge to detect and react to changes in the status of AWS Config events\.

You can create a rule that runs whenever there is a state transition, or when there is a transition to one or more states that are of interest\. Then, based on rules you create, Amazon EventBridge invokes one or more target actions when an event matches the values you specify in a rule\. Depending on the type of event, you might want to send notifications, capture event information, take corrective action, initiate events, or take other actions\. 

Before you create event rules for AWS Config, however, you should do the following: 
+ Familiarize yourself with events, rules, and targets in EventBridge\. For more information, see [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
+ For more information about how to get started with EventBridge and set up rules, see [Getting started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html)\.
+ Create the target or targets you will use in your event rules\.

**Topics**
+ [Amazon EventBridge format for AWS Config](#cloudwatch-event-format-for-awsconfig)
+ [Creating Amazon EventBridge Rule for AWS Config](#create-cloudwatch-events-rule-for-awsconfig)

## Amazon EventBridge format for AWS Config<a name="cloudwatch-event-format-for-awsconfig"></a>

The EventBridge [event](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html) for AWS Config has the following format:

```
          {
             "version": "0",
             "id": "cd4d811e-ab12-322b-8255-872ce65b1bc8",
             "detail-type": "event type",
             "source": "aws.config",
             "account": "111122223333",
             "time": "2018-03-22T00:38:11Z",
             "region": "us-east-1",
             "resources": [
                resources
             ],
             "detail": {
                specific message type
             }
          }
```

## Creating Amazon EventBridge Rule for AWS Config<a name="create-cloudwatch-events-rule-for-awsconfig"></a>

Use the following steps to create an EventBridge rule that triggers on an event emitted by AWS Config\. Events are emitted on a best effort basis\.

1. In the navigation pane, choose **Rules**\.

1. Choose **Create rule**\.

1. Enter a name and description for the rule\.

   A rule can't have the same name as another rule in the same Region and on the same event bus\.

1. For **Define pattern**, choose **Event pattern**\.

1. Choose **Pre\-defined pattern by service**

1. For **Service provider**, choose **AWS**\.

1. For **Service name**, choose **Config**\.

1. For **Event Type**, choose the event type that triggers the rule:
   + Choose **All Events** to make a rule that applies to all AWS services\. If you choose this option, you cannot choose specific message types, rule names, resource types, or resource IDs\.
   + Choose **AWS API Call via CloudTrail** to base rules on API calls made to this service\. For more information about creating this type of rule, see [Tutorial: Create an Amazon EventBridge rule for AWS CloudTrail API calls](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-ct-api-tutorial.html)\.
   + Choose **Config Configuration Item Change** to get notifications when a resource in your account changes\.

     As described in these support articles, you can use EventBridge to receive custom email notifications when a resource is created or deleted, [How can I receive custom email notifications when a resource is created in my AWS account using AWS Config service?](https://aws.amazon.com/premiumsupport/knowledge-center/config-email-resource-created/) and [How can I receive custom email notifications when a resource is deleted in my AWS account using AWS Config service?](https://aws.amazon.com/premiumsupport/knowledge-center/config-email-resource-deleted/)\.
   + Choose **Config Rules Compliance Change** to get notifications when a compliance check to your rules fails\.

     As described in this support article, you can use EventBridge to receive custom email notifications when a resource is non\-compliant, [How can I be notified when an AWS resource is non\-compliant using AWS Config?](https://aws.amazon.com/premiumsupport/knowledge-center/config-resource-non-compliant/)\.
   + Choose **Config Rules Re\-evaluation Status** to get reevaluation status notifications\. 
   + Choose **Config Configuration Snapshot Delivery Status** to get configuration snapshot delivery status notifications\.
   + Choose **Config Configuration History Delivery Status** to get configuration history delivery status notifications\.

1. Choose **Any message type** to receive notifications of any type\. Choose **Specific message type\(s\)** to receive the following types of notifications:
   + If you choose **ConfigurationItemChangeNotification**, you receive messages when the configuration of a resource that AWS Config evaluates has changed\.
   + If you choose **ComplianceChangeNotification**, you receive messages when the compliance type of a resource that AWS Config evaluates has changed\.
   + If you choose **ConfigRulesEvaluationStarted**, you receive messages when AWS Config starts evaluating your rule against the specified resources\.
   + If you choose **ConfigurationSnapshotDeliveryCompleted**, you receive messages when AWS Config successfully delivers the configuration snapshot to your Amazon S3 bucket\.
   + If you choose **ConfigurationSnapshotDeliveryFailed**, you receive messages when AWS Config fails to deliver the configuration snapshot to your Amazon S3 bucket\.
   + If you choose **ConfigurationSnapshotDeliveryStarted**, you receive messages when AWS Config starts delivering the configuration snapshot to your Amazon S3 bucket\.
   + If you choose **ConfigurationHistoryDeliveryCompleted**, you receive messages when AWS Config successfully delivers the configuration history to your Amazon S3 bucket\.

1. If you chose a specific event type from the **Event Type** dropdown list, choose **Any resource type** to make a rule that applies to all AWS Config supported resource types\.

   Or choose **Specific resource type\(s\)**, and then type the AWS Config supported resource type \(for example, `AWS::EC2::Instance`\)\.

1. If you chose a specific event type from the **Event Type** dropdown list, choose **Any resource ID** to include any AWS Config supported resource ID\.

   Or choose **Specific resource ID\(s\)**, and then type the AWS Config supported resource ID \(for example, `i-04606de676e635647`\)\.

1. If you chose a specific event type from the **Event Type** dropdown list, choose **Any rule name** to include any AWS Config supported rule\.

   Or choose **Specific rule name\(s\)**, and then type the AWS Config supported rule \(for example, **required\-tags**\)\.

1. For **Select event bus**, choose the event bus that you want to associate with this rule\. If you want this rule to match events that come from your account, select ** AWS default event bus**\. When an AWS service in your account emits an event, it always goes to your account’s default event bus\.

1. For **Select targets**, choose the type of target you have prepared to use with this rule, and then configure any additional options required by that type\.

1. The fields displayed vary depending on the service you choose\. Enter information specific to this target type as needed\.

1. For many target types, EventBridge needs permissions to send events to the target\. In these cases, EventBridge can create the IAM role needed for your rule to run\. 
   + To create an IAM role automatically, choose **Create a new role for this specific resource**\.
   + To use an IAM role that you created earlier, choose **Use existing role**\.

1. For **Retry policy and dead\-letter queue:**, under **Retry policy**:
   + For **Maximum age of event**, enter a value between one minute \(00:01\) and 24 hours \(24:00\)\.
   + For **Retry attempts**, enter a number between 0 and 185\.

1. For **Dead\-letter queue**, choose whether to use a standard Amazon SQS queue as a dead\-letter queue\. EventBridge sends events that match this rule to the dead\-letter queue if they are not successfully delivered to the target\. Do one of the following:
   + Choose **None** to not use a dead\-letter queue\.
   + Choose **Select an Amazon SQS queue in the current AWS account to use as the dead\-letter queue** and then select the queue to use from the dropdown list\.
   + Choose **Select an Amazon SQS queue in an other AWS account as a dead\-letter queue** and then enter the ARN of the queue to use\. You must attach a resource\-based policy to the queue that grants EventBridge permission to send messages to it\. For more information, see [Event retry policy and using dead\-letter queues](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-dlq.html)\.

1. \(Optional\) Choose **Add target** to add another target for this rule\.

1. \(Optional\) Enter one or more tags for the rule\. For more information, see [Amazon EventBridge tags](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tagging.html)\.

1. Review your rule setup to make sure it meets your event\-monitoring requirements\.

1. Choose **Create** to confirm your selection\.