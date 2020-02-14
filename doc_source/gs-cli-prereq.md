# Prerequisites<a name="gs-cli-prereq"></a>

Follow this procedure to create an Amazon S3 bucket, an Amazon SNS topic, and an IAM role with attached policies\. You can then use the AWS CLI to specify the bucket, topic, and role for AWS Config\.

**Contents**
+ [Creating an Amazon S3 Bucket](#gs-cli-create-s3bucket)
+ [Creating an Amazon SNS Topic](#gs-cli-create-snstopic)
+ [Creating an IAM Role](#gs-cli-create-iamrole)

## Creating an Amazon S3 Bucket<a name="gs-cli-create-s3bucket"></a>

If you already have an Amazon S3 bucket in your account and want to use it, skip this step and go to [Creating an Amazon SNS Topic](#gs-cli-create-snstopic)\.

To create an Amazon S3 bucket with the AWS CLI, use the [create\-bucket](https://docs.aws.amazon.com/cli/latest/reference/s3api/create-bucket.html) command\. 

**To create an Amazon S3 bucket with the console**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console\.aws\.amazon\.com/s3/](https://console.aws.amazon.com/s3/)\.

1. Choose **Actions** and then choose **Create Bucket**\.

1. For the **Bucket Name:**, type a name for your Amazon S3 bucket, such as *my\-config\-bucket*\. 
**Note**  
Make sure the bucket name you choose is unique across all existing bucket names in Amazon S3\. You cannot change the name of a bucket after it is created\. For more information on bucket naming rules and conventions, see [Bucket restrictions and Limitations](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html) in the *Amazon Simple Storage Service Developer Guide*\.

1. Choose **Create**\.

**Note**  
You can also use an Amazon S3 bucket from a different account, but you may need to create a policy for the bucket that grants access permissions to AWS Config\. For information on granting permissions to an Amazon S3 bucket, see [Permissions for the Amazon S3 Bucket](s3-bucket-policy.md), and then go to [Creating an Amazon SNS Topic](#gs-cli-create-snstopic)\.

## Creating an Amazon SNS Topic<a name="gs-cli-create-snstopic"></a>

If you already have an Amazon SNS topic in your account and want to use it, skip this step and go to [Creating an IAM Role](#gs-cli-create-iamrole)\.

To create an Amazon SNS topic with the AWS CLI, use the [create\-topic](https://docs.aws.amazon.com/cli/latest/reference/sns/create-topic.html) command\. 

**To create an Amazon SNS topic with the console**

1. Sign in to the AWS Management Console and open the Amazon SNS console at [https://console\.aws\.amazon\.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home)\.

1. Choose **Create New Topic**\.

1. For **Topic Name**, type a name for your SNS topic, such as *my\-config\-notice*\.

1. Choose **Create Topic**\. 

   The new topic appears in the **Topic Details** page\. Copy the **Topic ARN** for the next task\.

   For more information, see [ARN Format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-arns) in the *AWS General Reference*\.

To receive notifications from AWS Config, you must subscribe an email address to the topic\.

**To subscribe an email address to the SNS topic**

1. In the Amazon SNS console, choose **Subscriptions** in the navigation pane\.

1. On the **Subscriptions** page, choose **Create Subscription**\.

1. For **Topic ARN**, paste the topic ARN you copied in the previous task\.

1. For **Protocol**, choose **Email**\.

1. For **Endpoint**, type an email address that you can use to receive the notification and then choose **Subscribe**\.

1. Go to your email application and open the message from **AWS Notifications**\. Choose the link to confirm your subscription\.

   Your web browser displays a confirmation response from Amazon SNS\. Amazon SNS is now configured to receive notifications and send the notification as an email to the specified email address\. 

**Note**  
You can also use an Amazon SNS topic in a different account, but in that case you might need to create a policy for topic that grants access permissions to AWS Config\. For information on granting permissions to an Amazon SNS topic, see [Permissions for the Amazon SNS Topic](sns-topic-policy.md) and then go to [Creating an IAM Role](#gs-cli-create-iamrole)\.

## Creating an IAM Role<a name="gs-cli-create-iamrole"></a>

You can use the IAM console to create an IAM role that grants AWS Config permissions to access your Amazon S3 bucket, access your Amazon SNS topic, and get configuration details for supported AWS resources\. After you create the IAM role, you will create and attach policies to the role\. 

To create an IAM role with the AWS CLI, use the [create\-role](https://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html) command\. You can then attach a policy to the role with the [attach\-role\-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/attach-role-policy.html) command\.

**To create an IAM role with the console**

1. Sign in to the AWS Management Console and open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. In the IAM console, choose **Roles** in the navigation pane, and choose **Create New Role**\.

1. For **Role Name**, type a name that describes the purpose of this role\. Role names must be unique within your AWS account\. Because various entities might reference the role, you cannot edit the name of the role after you create it\. 

   Choose **Next Step**\.

1. Choose **AWS Service Roles**, and then choose **Select** for **AWS Config **\.

1. On the **Attach Policy** page, select **AWSConfigRole**\. This AWS managed policy grants AWS Config permission to get configuration details for supported AWS resources\. Then, choose **Next Step**\.

1. On the **Review** page, review the details about your role, and choose **Create Role**\.

1. On the **Roles** page, choose the role that you created to open its details page\.

You will expand the permissions in the role by creating inline policies that allow AWS Config to access your Amazon S3 bucket and your Amazon SNS topic\.

**To create an inline policy that grants AWS Config permission to access your Amazon S3 bucket**

1. In the **Permissions** section, expand the **Inline Policies** section, and choose **click here**\.

1. Choose **Custom Policy**, and choose **Select**\.

1. For **Policy Name**, type a name for your inline policy\.

1. Copy the example Amazon S3 bucket policy in [ IAM Role Policy for Amazon S3 Bucket](iamrole-permissions.md#iam-role-policies-S3-bucket) and paste it in the **Policy Document** editor\. 
**Important**  
Before you proceed to the next step, replace the following values in the policy\. If you do not replace the values, your policy will fail\.  
*myBucketName* – Replace with the name of your Amazon S3 bucket\.
*prefix* – Replace with your own prefix or leave blank by removing the trailing '/'\.
*myAccountID\-WithoutHyphens* – Replace with your AWS account ID\.

1. Choose **Apply Policy**\.

**To create an inline policy that grants AWS Config permissions to deliver notifications to your Amazon SNS topic**

1. In the **Permissions** section, expand the **Inline Policies** section, and choose **click here**\.

1. Choose **Custom Policy**, and choose **Select**\.

1. For **Policy Name**, type a name for your inline policy\.

1. Copy the Amazon SNS topic example policy in [ IAM Role Policy for Amazon SNS Topic](iamrole-permissions.md#iam-role-policies-sns-topic) and paste it in the **Policy Document** editor\.
**Important**  
Before you proceed to the next step, replace *arn:aws:sns:region:account\-id:myTopic* with the ARN you saved when you created your Amazon SNS topic\.

1. Choose **Apply Policy**\.