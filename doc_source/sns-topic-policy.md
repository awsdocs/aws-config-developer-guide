# Permissions for the Amazon SNS Topic<a name="sns-topic-policy"></a>

Use the information in this topic only if you want to configure AWS Config to deliver Amazon SNS topics owned by your account or by a different account\. AWS Config must have permissions to send notifications to an Amazon SNS topic\.

**Note**  
 AWS Config currently only supports same region and cross account access\. SNS topics used for remediation AWS Systems Manager documents \(SSM documents\) or for the recorder delivery channel cannot be cross\-region\.

**Contents**
+ [Required Permissions for the Amazon SNS Topic When Using IAM Roles](#required-permissions-snstopic-in-another-account)
+ [Required Permissions for the Amazon SNS Topic When Using Service\-Linked Roles](#required-permissions-snstopic-using-servicelinkedrole)
+ [Troubleshooting for the Amazon SNS Topic](#troubleshooting-for-snstopic-using-servicelinkedrole)

## Required Permissions for the Amazon SNS Topic When Using IAM Roles<a name="required-permissions-snstopic-in-another-account"></a>

You can attach a permission policy to the Amazon SNS topic owned by a different account\. If you want to use an Amazon SNS topic from another account, make sure to attach the following policy to an existing Amazon SNS topic\.

```
 {
  "Id": "Policy1415489375392",
  "Statement": [
    {
      "Sid": "AWSConfigSNSPolicy20150201",
      "Action": [
        "sns:Publish"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:sns:region:account-id:myTopic",
      "Principal": {
        "AWS": [
          "account-id1",
          "account-id2",
          "account-id3"
        ]
      }
    }
  ]
}
```

For the `Resource` key, *account\-id* is the AWS account number of the topic owner\. For *account\-id1*, *account\-id2*, and *account\-id3*, use the AWS accounts that will send data to an Amazon SNS topic\. You must substitute appropriate values for *region* and *myTopic*\.

When AWS Config sends a notification to an Amazon SNS topic, it first attempts to use the IAM role, but this attempt fails if the role or AWS account does not have permission to publish to the topic\. In this event, AWS Config sends the notification again, this time as AWS Config service principal\. Before the publication can succeed, the access policy for the topic must grant `sns:Publish` access to the `config.amazonaws.com` principal name\. You must attach an access policy, mentioned below, to the Amazon SNS topic to grant AWS Config access to the Amazon SNS topic in the event that the IAM role does not have permission to publish to the topic\.

## Required Permissions for the Amazon SNS Topic When Using Service\-Linked Roles<a name="required-permissions-snstopic-using-servicelinkedrole"></a>

The AWS Config service\-linked role does not have permission to publish messages to Amazon SNS topics\. So, if you set up AWS Config using a service\-linked role, AWS Config will send configuration items as the AWS Config service principal instead\. You will need to attach the following permission policy to the Amazon SNS topic in your own account or another account to grant AWS Config access to the Amazon SNS topic\.

```
{
"Id": "Policy_ID",
"Statement": [
  {
    "Sid": "AWSConfigSNSPolicy",
    "Effect": "Allow",
    "Principal": {
      "Service": "config.amazonaws.com"
    },
    "Action": "sns:Publish",
      "Resource": "arn:aws:sns:region:account-id:myTopic",
        "Condition" : {
        "StringEquals": {
          "AWS:SourceAccount": [
            "account-id1",
            "account-id2",
            "account-id3"
          ]
        }
      }
    }
  ]
}
```

For the `Resource` key, *account\-id* is the AWS account number of the topic owner\. For *account\-id1*, *account\-id2*, and *account\-id3*, use the AWS accounts that will send data to an Amazon SNS topic\. You must substitute appropriate values for *region* and *myTopic*\.

You can use the `AWS:SourceAccount` condition in the Amazon SNS topic policy above to restrict the Config service principal to only interact with the Amazon SNS topic when performing operations on behalf of specific accounts\.

AWS Config also supports the `AWS:SourceArn` condition which restricts the Config service principal to only interact with the Amazon S3 bucket when performing operations on behalf of specific AWS Config delivery channels\. When using the AWS Config service principal, the `AWS:SourceArn` property will always be set to `arn:aws:config:sourceRegion:sourceAccountID:*` where `sourceRegion` is the region of the delivery channel and `sourceAccountID` is the ID of the account containing the delivery channel\. For more information on AWS Config delivery channels, see [Managing the Delivery Channel](https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html)\. For example, add the following condition to restrict the Config service principal to interact with your Amazon S3 bucket only on behalf of a delivery channel in the `us-east-1` region in the account `123456789012`: `"ArnLike": {"AWS:SourceArn": "arn:aws:config:us-east-1:123456789012:*"}`\.

## Troubleshooting for the Amazon SNS Topic<a name="troubleshooting-for-snstopic-using-servicelinkedrole"></a>

AWS Config must have permissions to send notifications to an Amazon SNS topic\. If an Amazon SNS topic cannot receive notifications, verify that the IAM role that AWS Config was assuming must have `sns:Publish` permissions\. 