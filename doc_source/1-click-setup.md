# 1\-click setup<a name="1-click-setup"></a>

 AWS Config **1\-click setup** helps simplify the getting started process for AWS Config console customers by reducing the number of manual selections\.

**Note**  
 For more information about the **Get started** process, see [Manual setup](https://docs.aws.amazon.com/config/latest/developerguide/detailed-setup.html)\.

**To set up AWS Config with the console using **1\-click setup****

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.
**Note**  
If this is the first time that you are opening the AWS Config console, or you are setting up AWS Config in a new AWS Region, the AWS Config console page looks like the following image\.  
![\[The AWS Config getting started page provides an overview of the service.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/welcome.png)

1. Choose **1\-click setup**\. 

The set up page includes three steps, but through the **1\-click setup** workflow, you are automatically directed to Step 3 \(Review\)\. The following provides a breakdown of that procedure\.
+ Settings: To select the manner by which the AWS Config console records resources and roles, and choose where configuration history and configuration snapshot files are sent\.
+ Rules: For regions that support rules, this subsection is available for you to configure initial AWS managed rules that you can add to your account\.
**Note**  
After setting up, AWS Config will evaluate your AWS resources against the rules that you chose\. Additional rules can be created and existing ones can be updated in your account after setup\. For more information about rules, see [Managing your AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/setting-up-aws-config-rules-with-console.html)\.
+ Review: To verify your setup details\.

## Settings<a name="1-click-setup-settings.title"></a>

**General settings**

Under **Resource types to record**, the option to **Record all current and future resources supported in this region** is selected for you\. If you select this option, when AWS Config adds support for a new type of regional resource, it starts recording resources of that type automatically\. For more information, see [Supported Resource Types](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)\.

AWS Config records configuration changes for supported AWS resource types, and also third\-party resource types that are registered in the AWS CloudFormation registry\. AWS Config automatically starts recording new supported AWS resource types\. AWS Config also automatically starts recording third\-party resources and custom resource types that are managed through AWS CloudFormation\.

**Note**  
By default, the **1\-click setup** workflow does not include the option to **Include global resources** \(for example, AWS Identity and Access Management \(IAM\) resources\)\.

**Note**  
** High Number of AWS Config Evaluations**  
You may notice increased activity in your account during your initial month recording with AWS Config when compared to subsequent months\. During the initial bootstrapping process, AWS Config goes through all the resources in your account that you have selected for AWS Config to record\.  
If you are running ephemeral workloads, you may see increased activity from AWS Config as it records configuration changes associated with creating and deleting these temporary resources\. An ephemeral workload is a temporary use of computing resources that are loaded and run when needed\. Examples include Amazon Elastic Compute Cloud \(Amazon EC2\) spot instances, Amazon EMR jobs, and AWS Auto Scaling\. If you want to avoid the increased activity from running ephemeral workloads, you can run these types of workloads in a separate account with AWS Config turned off to avoid increased configuration recording and rule evaluations\.

The option to **Use an existing AWS Config service\-linked role** is selected for **AWS Config role**\.
+ Service\-linked roles are predefined by AWS Config and include all the permissions that the service requires to call other AWS services\.

**Delivery method**

**Choose a bucket from your account **is selected for you in this section\. This selection will default to the bucket in your account that is named in the format *config\-bucket\-**accountid*** \(for example, config\-bucket\-012345678901\)\. If you don't have a bucket created in that format, one will be created for you\.

For more information about S3 buckets, see [Buckets overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) in the *Amazon Simple Storage Service User Guide*\.

**Note**  
If you have not yet created an S3 bucket, go to [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the *Amazon Simple Storage Service User Guide*\.

## Rules<a name="1-click-setup-rules.title"></a>

Under **AWS Managed Rules**, no rules are selected for you at this step\. Instead, you are encouraged to create and update rules after you have finished setting up your account\.

## Review<a name="1-click-setup-review.title"></a>

Review your AWS Config setup details\. You can go back to edit changes for each section\. Choose **Confirm** to finish setting up AWS Config\.