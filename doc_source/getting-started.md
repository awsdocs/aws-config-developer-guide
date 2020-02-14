# Getting Started with AWS Config<a name="getting-started"></a>

When you sign up for AWS, your account has access to all AWS services\. You pay only for the services that you use\. 

If you do not have an AWS account, complete the following steps to create one\.

**To sign up for an AWS account**

1. Open [https://portal\.aws\.amazon\.com/billing/signup](https://portal.aws.amazon.com/billing/signup)\.

1. Follow the online instructions\.

   Part of the sign\-up procedure involves receiving a phone call and entering a verification code on the phone keypad\.

After you sign up for an AWS account, you can get started with AWS Config with the AWS Management Console, AWS CLI, or the AWS SDKs\. Use the console for a quick and streamlined process\.

When you set up AWS Config, you can complete the following:
+ Specify the resource types that you want AWS Config to record\.
+ Set up an Amazon S3 bucket to receive a configuration snapshot on request and configuration history\.
+ Set up an Amazon SNS topic to send configuration stream notifications\.
+ Grant AWS Config the permissions it needs to access the Amazon S3 bucket and the SNS topic\.
+ Specify the rules that you want AWS Config to use to evaluate compliance information for the recorded resource types\.

For more information about using the AWS CLI, see [Setting Up AWS Config with the AWS CLI](gs-cli.md)\. 

For more information about using the AWS SDKs, see [AWS Software Development Kits for AWS Config](cloudconfig-resources.md#config-aws-sdk)\.

**Topics**
+ [Setting Up AWS Config with the Console](gs-console.md)
+ [Setting Up AWS Config with the AWS CLI](gs-cli.md)
+ [Setting Up AWS Config Rules with the Console](setting-up-aws-config-rules-with-console.md)
+ [Viewing the AWS Config Dashboard](viewing-the-aws-config-dashboard.md)