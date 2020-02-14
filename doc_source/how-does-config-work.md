# How AWS Config Works<a name="how-does-config-work"></a>

When you turn on AWS Config, it first discovers the supported AWS resources that exist in your account and generates a [configuration item](config-concepts.md#config-items) for each resource\. 

 AWS Config also generates configuration items when the configuration of a resource changes, and it maintains historical records of the configuration items of your resources from the time you start the configuration recorder\. By default, AWS Config creates configuration items for every supported resource in the region\. If you don't want AWS Config to create configuration items for all supported resources, you can specify the resource types that you want it to track\. 

AWS Config keeps track of all changes to your resources by invoking the Describe or the List API call for each resource in your account\. The service uses those same API calls to capture configuration details for all related resources\. 

For example, removing an egress rule from a VPC security group causes AWS Config to invoke a Describe API call on the security group\. AWS Config then invokes a Describe API call on all of the instances associated with the security group\. The updated configurations of the security group \(the resource\) and of each instance \(the related resources\) are recorded as configuration items and delivered in a configuration stream to an Amazon Simple Storage Service \(Amazon S3\) bucket\. 

AWS Config also tracks the configuration changes that were not initiated by the API\. AWS Config examines the resource configurations periodically and generates configuration items for the configurations that have changed\. 

If you are using AWS Config rules, AWS Config continuously evaluates your AWS resource configurations for desired settings\. Depending on the rule, AWS Config will evaluate your resources either in response to configuration changes or periodically\. Each rule is associated with an AWS Lambda function, which contains the evaluation logic for the rule\. When AWS Config evaluates your resources, it invokes the rule's AWS Lambda function\. The function returns the compliance status of the evaluated resources\. If a resource violates the conditions of a rule, AWS Config flags the resource and the rule as noncompliant\. When the compliance status of a resource changes, AWS Config sends a notification to your Amazon SNS topic\. 

![\[How AWS Config works.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/how-AWSconfig-works.png)

## Deliver Configuration Items<a name="delivery-channel"></a>

AWS Config can deliver configuration items through one of the following channels:

### Amazon S3 Bucket<a name="delivery-channel-S3-bucket"></a>

AWS Config tracks changes in the configuration of your AWS resources, and it regularly sends updated configuration details to an Amazon S3 bucket that you specify\. For each resource type that AWS Config records, it sends a *configuration history file* every six hours\. Each configuration history file contains details about the resources that changed in that six\-hour period\. Each file includes resources of one type, such as Amazon EC2 instances or Amazon EBS volumes\. If no configuration changes occur, AWS Config does not send a file\.

AWS Config sends a *configuration snapshot* to your Amazon S3 bucket when you use the [deliver\-config\-snapshot](https://docs.aws.amazon.com/cli/latest/reference/configservice/deliver-config-snapshot.html) command with the AWS CLI, or when you use the [DeliverConfigSnapshot](https://docs.aws.amazon.com/config/latest/APIReference/API_DeliverConfigSnapshot.html) action with the AWS Config API\. A configuration snapshot contains configuration details for all resources that AWS Config records in your AWS account\. The configuration history file and configuration snapshot are in JSON format\.

**Note**  
AWS Config only delivers the configuration history files and configuration snapshots to the specified S3 bucket; AWS Config doesn't modify the lifecycle policies for objects in the S3 bucket\. You can use lifecycle policies to specify whether you want to delete or archive objects to Amazon S3 Glacier\. For more information, see [Managing Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/LifecycleConfiguration.html) in the *Amazon Simple Storage Service Console User Guide*\. You can also see the [Archiving Amazon S3 Data to S3 Glacier](https://aws.amazon.com/blogs/aws/archive-s3-to-glacier/) blog post\.

### Amazon SNS Topic<a name="delivery-channel-SNS-topic"></a>

An Amazon Simple Notification Service \(Amazon SNS\) topic is a communication channel that Amazon SNS uses to deliver messages \(or *notifications*\) to subscribing endpoints such as an email address or clients\. Other types of Amazon SNS notifications include push notification messages to apps on mobile phones, Short Message Service \(SMS\) notifications to SMS\-enabled mobile phones and smart phones, and HTTP POST requests\. For best results, use Amazon SQS as the notification endpoint for the SNS topic and then process the information in the notification programmatically\.

AWS Config uses the Amazon SNS topic that you specify to send you notifications\. The type of notification that you are receiving is indicated by the value for the `messageType` key in the message body, as in the following example:

```
"messageType": "ConfigurationHistoryDeliveryCompleted"
```

The notifications can be any of the following message types:

`ComplianceChangeNotification`  
The compliance type of a resource that AWS Config evaluates has changed\. The compliance type indicates whether the resource complies with a specific AWS Config rule, and it is represented by the `ComplianceType` key in the message\. The message includes `newEvaluationResult` and `oldEvaluationResult` objects for comparison\.

`ConfigRulesEvaluationStarted`  
AWS Config started evaluating your rule against the specified resources\.

`ConfigurationSnapshotDeliveryStarted`  
AWS Config started delivering the configuration snapshot to your Amazon S3 bucket\. The name of the Amazon S3 bucket is provided for the `s3Bucket` key in the message\.

`ConfigurationSnapshotDeliveryCompleted`  
AWS Config successfully delivered the configuration snapshot to your Amazon S3 bucket\.

`ConfigurationSnapshotDeliveryFailed`  
AWS Config failed to deliver the configuration snapshot to your Amazon S3 bucket\.

`ConfigurationHistoryDeliveryCompleted`  
AWS Config successfully delivered the configuration history to your Amazon S3 bucket\.

`ConfigurationItemChangeNotification`  
A resource has been created, deleted, or changed in configuration\. This message includes the details of the configuration item that AWS Config creates for this change, and it includes the type of change\. These notifications are delivered within minutes of a change and are collectively known as the *configuration stream*\.

`OversizedConfigurationItemChangeNotification`  
This message type is delivered when a configuration item change notification exceeded the maximum size allowed by Amazon SNS\. The message includes a summary of the configuration item\. You can view the complete notification in the specified Amazon S3 bucket location\.

`OversizedConfigurationItemChangeDeliveryFailed`  
AWS Config failed to deliver the oversized configuration item change notification to your Amazon S3 bucket\.

For example notifications, see [Notifications that AWS Config Sends to an Amazon SNS topic](notifications-for-AWS-Config.md)\.

For more information about Amazon SNS, see the [Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/)\.