# Setting Up AWS Config with the Console<a name="gs-console"></a>

You can use the AWS Management Console to get started with AWS Config to do the following: 
+ Specify the resource types you want AWS Config to record\.
+ Set up Amazon SNS to notify you of configuration changes\.
+ Specify an Amazon S3 bucket to receive configuration information\.
+ Add AWS Config managed rules to evaluate resource types\.

If you are using AWS Config for the first time or configuring AWS Config for a new region, you can choose managed rules to evaluate resource configurations\. For regions that support AWS Config and AWS Config Rules, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\.

**To set up AWS Config with the console**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. If this is the first time you are opening the AWS Config console or you are setting up AWS Config in a new region, the AWS Config console page looks like the following:   
![\[The AWS Config getting started page provides an overview of the service.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/welcome.png)

1. Choose **1\-click setup** to launch AWS Config based on AWS best practices\. You can also choose **Get started** to go through the following steps yourself\.

1. On the **Settings** page, for **Resource types to record**, specify all the resource types you want AWS Config to record\. These resource types are AWS resources or third\-party resources or custom resources\.
   + **Record all resources supported in this region**
     + AWS Config records configuration changes for supported AWS resource types as well as third\-party resource types registered in the AWS CloudFormation registry\. AWS Config automatically starts recording new supported AWS resource types\. AWS Config also atuomatically starts recording third\-party resources and custom resource types are that managed through AWS CloudFormation\.
     + Choose **Include global resources** to record supported global resources types \(such as IAM resources\)\. AWS Config automatically starts recording new supported global resource types\.
   + **Record specific resource types**
     + AWS Config records configuration changes for only the resource types that you specify\.

   For more information about these options, see [Selecting Which Resources AWS Config Records](select-resources.md)\.

1. For **AWS Config role**, choose either an existing AWS Config service\-linked role or choose a role from your account by entering your account ID\. Service\-linked roles are predefined by AWS Config and include all the permissions that the service requires to call other AWS services\.

1. For **Delivery method**, choose the Amazon S3 bucket to which AWS Config sends configuration history and configuration snapshot files:
   + **Create a bucket** – For **S3 bucket name**, type a name for your Amazon S3 bucket\. 

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

1. 

   If you are setting up AWS Config in a region that supports rules, choose **Next**\. See [Setting Up AWS Config Rules with the Console](setting-up-aws-config-rules-with-console.md)\. 

   Otherwise, choose **Confirm**\.

For information about looking up the existing resources in your account and understanding the configurations of your resources, see [Viewing AWS Resource Configurations and History](view-manage-resource.md)\.

You can also use Amazon Simple Queue Service to monitor AWS resources programmatically\. For more information, see [Monitoring AWS Resource Changes with Amazon SQS](security-logging-and-monitoring.md#monitor-resource-changes)\.