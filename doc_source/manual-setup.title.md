# Manual setup<a name="manual-setup.title"></a>

With the **Get started** workflow, you can go through all the manual selections of the setup process to get started with the AWS Config console\.

**Note**  
 For more information about the **1\-click setup** process, see [1\-click setup](https://docs.aws.amazon.com/config/latest/developerguide/1-click-setup.html)\.

**To set up AWS Config with the console using **Get started****

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.
**Note**  
If this is the first time that you are opening the AWS Config console, or you are setting up AWS Config in a new AWS Region, the AWS Config console page looks like the following image\.   
![\[The AWS Config getting started page provides an overview of the service.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/welcome.png)

1. Choose **Get started**\. 

The setup page includes three steps\. The following provides a breakdown of that procedure after you choose **Get started**\.
+ Settings: To select the manner by which the AWS Config console records resources and roles, and choose where configuration history and configuration snapshot files are sent\.
+ Rules: For Regions that support rules, this subsection is available for you to configure initial AWS managed rules that you can add to your account\.
**Note**  
After setting up, AWS Config will evaluate your AWS resources against the rules that you chose\. Additional rules can be created and existing ones can be updated and in your account after setup\. For more information about rules, see [Managing your AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/setting-up-aws-config-rules-with-console.html)\.
+ Review: To verify your setup details\.

## Settings<a name="gs-settings.title"></a>

**General settings**

## <a name="gs-console-settings"></a>

1. On the **Settings** page, for **Resource types to record**, specify all the resource types you want AWS Config to record\. These resource types are AWS resources or third\-party resources or custom resources\. For more information about the following options, see [Selecting Which Resources AWS Config Records](select-resources.md)\.
   + **Record all current and future resources supported in this region**
     + AWS Config records configuration changes for supported AWS resource types as well as third\-party resource types registered in the AWS CloudFormation registry\. AWS Config automatically starts recording new supported AWS resource types\. AWS Config also automatically starts recording third\-party resources and custom resource types that are managed through AWS CloudFormation\. For more information, see [Supported Resource Types](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)\.
     + Choose **Include global resources** to record supported global resources types \(such as IAM resources\)\. AWS Config automatically starts recording new supported global resource types\.
**Important**  
Global resource types onboarded to AWS Config recording after February 2022 will only be recorded in the service's home region for the commercial partition and AWS GovCloud \(US\-West\) for the GovCloud partition\. You can view the Configuration Items for these new global resource types only in their home region and AWS GovCloud \(US\-West\)\.   
Supported global resource types onboarded before February 2022 such as `AWS::IAM::Group`, `AWS::IAM::Policy`, `AWS::IAM::Role`, `AWS::IAM::User` remain unchanged, and they will continue to deliver Configuration Items in all supported regions in AWS Config\. The change will only affect new global resource types onboarded after February 2022\.
   + **Record specific resource types**
     + AWS Config records configuration changes for only the resource types that you specify\.
**Note**  
** High Number of AWS Config Evaluations**  
You may notice increased activity in your account during your initial month recording with AWS Config when compared to subsequent months\. During the initial bootstrapping process, AWS Config goes through all the resources in your account that you have selected for AWS Config to record\.  
If you are running ephemeral workloads, you may see increased activity from AWS Config as it records configuration changes associated with creating and deleting these temporary resources\. An ephemeral workload is a temporary use of computing resources that are loaded and run when needed\. Examples include Amazon Elastic Compute Cloud \(Amazon EC2\) spot instances, Amazon EMR jobs, and AWS Auto Scaling\. If you want to avoid the increased activity from running ephemeral workloads, you can run these types of workloads in a separate account with AWS Config turned off to avoid increased configuration recording and rule evaluations\.

1. For **AWS Config role**, choose either an existing AWS Config service\-linked role or choose a role from your account\. 
   + Service\-linked roles are predefined by AWS Config and include all the permissions that the service requires to call other AWS services\.
**Note**  
**Service\-linked role**  
If you haven't yet added a service\-linked role, one will be added for you\.  
**Pre\-existing AWS Config role**  
If you have used an AWS service that uses AWS Config, such as AWS Security Hub or AWS Control Tower, and an AWS Config role has already been created, make sure that the IAM role that you use when setting up AWS Config keeps the same minimum permissions as the already created AWS Config role\. You must do this so that the other AWS service continues to run as expected\.   
For example, if AWS Control Tower has an IAM role that allows AWS Config to read Amazon Simple Storage Service \(Amazon S3\) objects, make sure that the same permissions are granted within the IAM role you use when setting up AWS Config\. Otherwise, it may interfere with how AWS Control Tower operates\. For more information about IAM roles for AWS Config, see [AWS Identity and Access Management](https://docs.aws.amazon.com/config/latest/developerguide/security-iam.html)\. 

**Delivery method**

## <a name="gs-console-delivery-method"></a>

1. For **Delivery method**, choose the S3 bucket to which AWS Config sends configuration history and configuration snapshot files:
   + **Create a bucket** – For **S3 bucket name**, type a name for your S3 bucket\. 

     The name that you type must be unique across all existing bucket names in Amazon S3\. One way to help ensure uniqueness is to include a prefix; for example, the name of your organization\. You can't change the bucket name after it is created\. For more information, see [Bucket Restrictions and Limitations](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html) in the *Amazon Simple Storage Service User Guide*\. 
   + **Choose a bucket from your account** – For **S3 bucket name**, choose your preferred bucket\.
   + **Choose a bucket from another account** – For **S3 bucket name**, type the bucket name\.
**Note**  
If you choose a bucket from another account, that bucket must have policies that grant access permissions to AWS Config\. For more information, see [Permissions for the Amazon S3 Bucket](s3-bucket-policy.md)\.

1. For **Amazon SNS topic**, choose **Stream configuration changes and notifications to an Amazon SNS topic** to have AWS Config send notifications such as configuration history delivery, configuration snapshot delivery, and compliance\. 

1. If you chose to have AWS Config stream to an Amazon SNS topic, choose the target topic:
   + **Create a topic** – For **Topic Name**, type a name for your SNS topic\.
   + **Choose a topic from your account** – For **Topic Name**, select your preferred topic\.
   + **Choose a topic from another account** – For **Topic ARN**, type the Amazon Resource Name \(ARN\) of the topic\. If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config\. For more information, see [Permissions for the Amazon SNS Topic](sns-topic-policy.md)\.
**Note**  
The Amazon SNS topic must exist in the same region as the region in which you set up AWS Config\.

## Rules<a name="manual-setup-rules.title"></a>

## <a name="setting-up-rules.title"></a>

If you are setting up AWS Config in a region that supports rules, choose **Next**\. For more information, see [Managing Your AWS Config Rules](evaluate-config_manage-rules.md)\. 

Otherwise, choose **Confirm**\.

## Review<a name="manual-setup-review.title"></a>

Review your AWS Config set up details\. You can go back to edit changes for each section\. Choose **Confirm** to finish setting up AWS Config\.

## For more information<a name="manual-setup-more-info.title"></a>

## <a name="manual-setup-more-info.title"></a>

For information about looking up the existing resources in your account and understanding the configurations of your resources, see [Viewing AWS Resource Configurations and History](view-manage-resource.md)\.

You can also use Amazon Simple Queue Service to monitor AWS resources programmatically\. For more information, see [Monitoring AWS Resource Changes with Amazon SQS](monitor-resource-changes.md)\.