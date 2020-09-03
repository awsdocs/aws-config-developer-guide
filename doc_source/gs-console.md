# Setting Up AWS Config with the Console<a name="gs-console"></a>

You can use the AWS Management Console to get started with AWS Config to do the following: 
+ Specify the resource types you want AWS Config to record\.
+ Set up Amazon SNS to notify you of configuration changes\.
+ Specify an Amazon S3 bucket to receive configuration information\.
+ Add AWS Config managed rules to evaluate the resource types\.

If you are using AWS Config for the first time or configuring AWS Config for a new region, you can choose managed rules to evaluate resource configurations\. For regions that support AWS Config and AWS Config Rules, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\.

**To set up AWS Config with the console**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. If this is the first time you are opening the AWS Config console or you are setting up AWS Config in a new region, the AWS Config console page looks like the following:   
![\[The AWS Config getting started page provides an overview of the service.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/welcome.png)

1. Choose **Get Started Now**\.

1. On the **Settings** page, for **Resource types to record**, specify all the resource types you want AWS Config to record\. These resource types are AWS resources or third\-party resources or custom resources\.
   + **All resources** – AWS Config records all supported resources with the following options:
     + **Record all resources supported in this region** – AWS Config records configuration changes for supported AWS resource types as well as third\-party resource types registered in AWS CloudFormation registry\. AWS Config automatically starts recording new supported AWS resource types\. It also automatically starts recording third\-party resource types that are managed \(i\.e\. created/updated/deleted\) through AWS CloudFormation\.
     + **Include global resources** – AWS Config includes supported types of global resources with the resources that it records \(for example, IAM resources\)\. When AWS Config adds support for a new global resource type, AWS Config automatically starts recording resources of that type\.
   + **Specific types** – AWS Config records configuration changes for only the resource types that you specify\.

   For more information about these options, see [Selecting Which Resources AWS Config Records](select-resources.md)\.

1. For **Amazon S3 Bucket**, choose the Amazon S3 bucket to which AWS Config sends configuration history and configuration snapshot files:
   + **Create a new bucket** – For **Bucket Name**, type a name for your Amazon S3 bucket\. 

     The name that you type must be unique across all existing bucket names in Amazon S3\. One way to help ensure uniqueness is to include a prefix; for example, the name of your organization\. You can't change the bucket name after it is created\. For more information, see [Bucket Restrictions and Limitations](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html) in the *Amazon Simple Storage Service Developer Guide*\. 
   + **Choose a bucket from your account** – For **Bucket Name**, choose your preferred bucket\.
   + **Choose a bucket from another account** – For **Bucket Name**, type the bucket name\.

     If you choose a bucket from another account, that bucket must have policies that grant access permissions to AWS Config\. For more information, see [Permissions for the Amazon S3 Bucket](s3-bucket-policy.md)\.

1. For **Amazon SNS Topic**, choose whether AWS Config streams information by selecting the **Stream configuration changes and notifications to an Amazon SNS topic**\. AWS Config sends notifications such as configuration history delivery, configuration snapshot delivery, and compliance\. 

1. If you chose to have AWS Config stream to an Amazon SNS topic, choose the target topic:
   + **Create a new topic** – For **Topic Name**, type a name for your SNS topic\.
   + **Choose a topic from your account** – For **Topic Name**, select your preferred topic\.
   + **Choose a topic from another account** – For **Topic ARN**, type the Amazon Resource Name \(ARN\) of the topic\. If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config\. For more information, see [Permissions for the Amazon SNS Topic](sns-topic-policy.md)\.
**Note**  
The Amazon SNS topic must exist in the same region as the region in which you set up AWS Config\.

1. For **AWS Config role**, choose the IAM role that grants AWS Config permission to record configuration information and send this information to Amazon S3 and Amazon SNS:
   + **Create a role** – AWS Config creates a role that has the required permissions\. For **Role name**, you can customize the name that AWS Config creates\.
   + **Choose a role from your account** – For **Role name**, choose an IAM role in your account\. AWS Config will attach the required policies\. For more information, see [Permissions for the IAM Role Assigned to AWS Config](iamrole-permissions.md)\.
**Note**  
Check the box if you want to use the IAM role as is\. AWS Config will not attach policies to the role\.

1. If you are setting up AWS Config in a region that supports rules, choose **Next**\. See [Setting Up AWS Config Rules with the Console](setting-up-aws-config-rules-with-console.md)\. 

   Otherwise, choose **Save**\. AWS Config displays the **Resource inventory** page\.

For information about looking up the existing resources in your account and understanding the configurations of your resources, see [Viewing AWS Resource Configurations and History](view-manage-resource.md)\.

You can also use Amazon Simple Queue Service to monitor AWS resources programmatically\. For more information, see [Monitoring AWS Resource Changes with Amazon SQS](monitor-resource-changes.md)\.