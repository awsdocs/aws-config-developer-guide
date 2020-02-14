# Monitoring AWS Resource Changes with Amazon SQS<a name="monitor-resource-changes"></a>

AWS Config uses Amazon Simple Notification Service \(SNS\) to send you notifications every time a supported AWS resource is created, updated, or otherwise modified as a result of user API activity\. However, you might be interested in only certain resource configuration changes\. For example, you might consider it critical to know when someone modifies the configuration of a security group, but not need to know every time there is a change to tags on your Amazon EC2 instances\. Or, you might want to write a program that performs specific actions when specific resources are updated\. For example, you might want to start a certain workflow when a security group configuration is changed\. If you want to programmatically consume the data from AWS Config in these or other ways, use an Amazon Simple Queue Service queue as the notification endpoint for Amazon SNS\.

**Note**  
Notifications can also come from Amazon SNS in the form of an email, a Short Message Service \(SMS\) message to SMS\-enabled mobile phones and smartphones, a notification message to an application on a mobile device, or a notification message to one or more HTTP or HTTPS endpoints\.

You can have a single SQS queue subscribe to multiple topics, whether you have one topic per region or one topic per account per region\. You must subscribe the queue to your desired SNS topic\. \(You can subscribe multiple queues to one SNS topic\.\) For more information, see [Sending Amazon SNS Messages to Amazon SQS Queues](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToSQS.html)\.

## Permissions for Amazon SQS<a name="sqs-policy"></a>

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
        "Principal": "*",
        "Action": "sqs:*",
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