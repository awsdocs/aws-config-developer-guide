# Getting Started with AWS Config<a name="getting-started"></a>

AWS Config provides a detailed view of the configuration of AWS resources in your AWS account\. With AWS Config, you can review changes in configurations and relationships between AWS resources, explore resource configuration history, and use rules to determine compliance\. For more information, see [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) and [How AWS Config Works](https://docs.aws.amazon.com/config/latest/developerguide/how-does-config-work.html)\.

## Features<a name="getting-started-features"></a>

When you set up AWS Config, you can complete the following:

**Resource management**
+ Specify the resource types you want AWS Config to record\.
+ Set up an Amazon S3 bucket to receive a configuration snapshot on request and configuration history\.
+ Set up Amazon SNS to send configuration stream notifications\.
+ Grant AWS Config the permissions it needs to access the Amazon S3 bucket and the Amazon SNS topic\.

  For more information, see [Viewing AWS Resource Configurations and History](https://docs.aws.amazon.com/config/latest/developerguide/view-manage-resource.html) and [Managing AWS Resource Configurations and History](https://docs.aws.amazon.com/config/latest/developerguide/manage-config.html)\.

**Rules and conformance packs**
+ Specify the rules that you want AWS Config to use to evaluate compliance information for the recorded resource types\.
+ Use conformance packs, or a collection of AWS Config rules and remediation actions that can be deployed and monitored as a single entity in your AWS account\.

  For more information, see [Evaluating Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) and [Conformance Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html)\.

**Aggregators**
+ Use an aggregator to get a centralized view of your resource inventory and compliance\. An aggregator is an AWS Config resource type that collects AWS Config configuration and compliance data from multiple AWS accounts and AWS Regions into a single account and Region\.

  For more information, see [Multi\-Account Multi\-Region Data Aggregation ](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html)\.

**Advanced queries**
+ Use one of the sample queries or write your own query by referring to the configuration schema of the AWS resource\.

  For more information, see [Querying the Current Configuration State of AWS Resources ](https://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html)\. 

## Signing up for AWS<a name="getting-started-signing-up"></a>

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Create an administrative user](#create-an-admin)

### Sign up for an AWS account<a name="sign-up-for-aws"></a>

If you do not have an AWS account, complete the following steps to create one\.

**To sign up for an AWS account**

1. Open [https://portal\.aws\.amazon\.com/billing/signup](https://portal.aws.amazon.com/billing/signup)\.

1. Follow the online instructions\.

   Part of the sign\-up procedure involves receiving a phone call and entering a verification code on the phone keypad\.

   When you sign up for an AWS account, an *AWS account root user* is created\. The root user has access to all AWS services and resources in the account\. As a security best practice, [assign administrative access to an administrative user](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html), and use only the root user to perform [tasks that require root user access](https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html)\.

AWS sends you a confirmation email after the sign\-up process is complete\. At any time, you can view your current account activity and manage your account by going to [https://aws\.amazon\.com/](https://aws.amazon.com/) and choosing **My Account**\.

### Create an administrative user<a name="create-an-admin"></a>

After you sign up for an AWS account, create an administrative user so that you don't use the root user for everyday tasks\.

**Secure your AWS account root user**

1.  Sign in to the [AWS Management Console](https://console.aws.amazon.com/) as the account owner by choosing **Root user** and entering your AWS account email address\. On the next page, enter your password\.

   For help signing in by using root user, see [Signing in as the root user](https://docs.aws.amazon.com/signin/latest/userguide/console-sign-in-tutorials.html#introduction-to-root-user-sign-in-tutorial) in the *AWS Sign\-In User Guide*\.

1. Turn on multi\-factor authentication \(MFA\) for your root user\.

   For instructions, see [Enable a virtual MFA device for your AWS account root user \(console\)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html#enable-virt-mfa-for-root) in the *IAM User Guide*\.

**Create an administrative user**
+ For your daily administrative tasks, grant administrative access to an administrative user in AWS IAM Identity Center \(successor to AWS Single Sign\-On\)\.

  For instructions, see [Getting started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in the *AWS IAM Identity Center \(successor to AWS Single Sign\-On\) User Guide*\.

**Sign in as the administrative user**
+ To sign in with your IAM Identity Center user, use the sign\-in URL that was sent to your email address when you created the IAM Identity Center user\.

  For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](https://docs.aws.amazon.com/signin/latest/userguide/iam-id-center-sign-in-tutorial.html) in the *AWS Sign\-In User Guide*\.

## Using AWS Config<a name="getting-started-using-aws-config"></a>

After you sign up for an AWS account, you can get started with AWS Config with the AWS Management Console, AWS CLI, or the AWS SDKs\. For more information about using the AWS CLI or AWS SDKs, see [Setting Up AWS Config with the AWS CLI](gs-cli.md) and [AWS Software Development Kits for AWS Config](cloudconfig-resources.md#config-aws-sdk)\.

You can also use the console for a quick and streamlined process\. For more information, see [Setting Up AWS Config with the Console](gs-console.md)\.

**Topics**
+ [Setting Up AWS Config with the Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html)
+ [Setting Up AWS Config with the AWS CLI](https://docs.aws.amazon.com/config/latest/developerguide/gs-cli.html)
+ [Using this service with an AWS SDK](https://docs.aws.amazon.com/config/latest/developerguide/sdk-general-information-section.html)
+ [Using AWS Config Rules with the Console](https://docs.aws.amazon.com/config/latest/developerguide/setting-up-aws-config-rules-with-console.html)