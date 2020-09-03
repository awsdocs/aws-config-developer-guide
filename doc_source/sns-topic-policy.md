# Permissions for the Amazon SNS Topic<a name="sns-topic-policy"></a>

Use the information in this topic only if you want to configure AWS Config to deliver Amazon SNS topics owned by your account or by a different account\. AWS Config must have permissions to send notifications to an Amazon SNS topic\.

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
        "SNS:Publish"
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

For the `Resource` key, *account\-id* is the account number of the topic owner\. For *account\-id1*, *account\-id2*, and *account\-id3*, use the AWS accounts that will send data to an Amazon SNS topic\. You must substitute appropriate values for *region* and *myTopic*\. 

## Required Permissions for the Amazon SNS Topic When Using Service\-Linked Roles<a name="required-permissions-snstopic-using-servicelinkedrole"></a>

If you set up AWS Config using a service\-linked role, you need to attach a permission policy to the Amazon SNS topic\. If you want to use an Amazon SNS topic from your own account, make sure to attach the following policy to an existing Amazon SNS topic\.

```
{
  "Id": "Policy_ID",
  "Statement": [
    {
      "Sid": "AWSConfigSNSPolicy",
      "Effect": "Allow",
      "Principal": {
        "AWS": "[configRoleArn]"
      },
      "Action": "SNS:Publish",
      "Resource": "arn:aws:sns:region:account-id:myTopic",
    }
  ]
}
```

You must substitute appropriate values for *region*, *account\-id*, and *myTopic*\.

**Note**  
AWS Config does not recommend using a service\-linked role when using Amazon SNS topic from other accounts\.

## Troubleshooting for the Amazon SNS Topic<a name="troubleshooting-for-snstopic-using-servicelinkedrole"></a>

AWS Config must have permissions to send notifications to an Amazon SNS topic\. If an Amazon SNS topic cannot receive notifications, verify that the IAM role that AWS Config was assuming must have `sns:publish` permissions\. 