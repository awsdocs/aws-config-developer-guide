# Permissions for the Amazon S3 Bucket<a name="s3-bucket-policy"></a>

By default, all Amazon S3 buckets and objects are private\. Only the resource owner which is the AWS account that created the bucket can access that bucket\. The resource owner can, however, choose to grant access permissions to other resources and users\. One way to do this is to write an access policy\.

If AWS Config creates an Amazon S3 bucket for you automatically \(for example, if you use AWS Config console to set up your delivery channel\), these permissions are automatically added to Amazon S3 bucket\. However, if you specify an existing Amazon S3 bucket, you must ensure that the S3 bucket has the correct permissions\.

**Note**  
An object does not inherit the permissions from its bucket\. For example, if you create a bucket and grant write access to a user, you can't access that user’s objects unless the user explicitly grants you access\.

**Contents**
+ [Required Permissions for the Amazon S3 Bucket When Using IAM Roles](#required-permissions-in-another-account)
+ [Required Permissions for the Amazon S3 Bucket When Using Service\-Linked Roles](#required-permissions-using-servicelinkedrole)
+ [Granting AWS Config access to the Amazon S3 Bucket](#granting-access-in-another-account)

## Required Permissions for the Amazon S3 Bucket When Using IAM Roles<a name="required-permissions-in-another-account"></a>

When AWS Config sends configuration information \(history files and snapshots\) to Amazon S3 bucket in your account, it assumes the IAM role that you assigned when you set up AWS Config\. When AWS Config sends configuration information to an Amazon S3 bucket in another account, it first attempts to use the IAM role, but this attempt fails if the access policy for the bucket does not grant `WRITE` access to the IAM role\. In this event, AWS Config sends the information again, this time as the AWS Config service principal\. Before the delivery can succeed, the access policy must grant `WRITE` access to the `config.amazonaws.com` principal name\. AWS Config is then the owner of the objects it delivers to the S3 bucket\. You must attach an access policy, mentioned in step 6 below to the Amazon S3 bucket in another account to grant AWS Config access to the Amazon S3 bucket\.

Before AWS Config can deliver logs to your Amazon S3 bucket AWS Config checks whether the bucket exists and in which AWS region the bucket is located\. AWS Config attempts to call Amazon S3 [HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RESTBucketHEAD.html) API to check whether the bucket exists and to get the bucket region\. If permissions are not provided to locate the bucket when the location check is performed, you see `AccessDenied` error in AWS CloudTrail logs\. However, the log delivery to your Amazon S3 bucket succeeds if you do not provide bucket location permissions\.

## Required Permissions for the Amazon S3 Bucket When Using Service\-Linked Roles<a name="required-permissions-using-servicelinkedrole"></a>

The AWS Config service\-linked role does not have permission to put objects to Amazon S3 buckets\. So, if you set up AWS Config using a service\-linked role, AWS Config will send configuration items as the AWS Config service principal instead\. You will need to attach an access policy, mentioned in step 6 below, to the Amazon S3 bucket in your own account or another account to grant AWS Config access to the Amazon S3 bucket\.

## Granting AWS Config access to the Amazon S3 Bucket<a name="granting-access-in-another-account"></a>

Follow these steps to add an access policy to the Amazon S3 bucket in your own account or another account\. The access policy allows AWS Config to send configuration information to the Amazon S3 bucket\.

1. Sign in to the AWS Management Console using the account that has the S3 bucket\.

1. Open the Amazon S3 console at [https://console\.aws\.amazon\.com/s3/](https://console.aws.amazon.com/s3/)\.

1. Select the bucket that you want AWS Config to use to deliver configuration items, and then choose **Properties**\. 

1. Choose **Permissions**\.

1. Choose **Edit Bucket Policy**\.

1. Copy the following policy into the **Bucket Policy Editor** window:
**Important**  
As a security best practice when allowing AWS Config access to an Amazon S3 bucket, we strongly recommend that you restrict access in the bucket policy with the `AWS:SourceAccount` condition\. If your existing bucket policy does not follow this security best practice, we strongly recommened you edit that bucket policy to include this protection\. This makes sure that AWS Config is granted access on behalf of expected users only\.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AWSConfigBucketPermissionsCheck",
         "Effect": "Allow",
         "Principal": {
           "Service": "config.amazonaws.com"
         },
         "Action": "s3:GetBucketAcl",
         "Resource": "arn:aws:s3:::targetBucketName",
         "Condition": { 
           "StringEquals": {
             "AWS:SourceAccount": "sourceAccountID"
           }
         }
       },
       {
         "Sid": "AWSConfigBucketExistenceCheck",
         "Effect": "Allow",
         "Principal": {
           "Service": "config.amazonaws.com"
         },
         "Action": "s3:ListBucket",
         "Resource": "arn:aws:s3:::targetBucketName",
         "Condition": { 
           "StringEquals": {
             "AWS:SourceAccount": "sourceAccountID"
           }
         }
       },
       {
         "Sid": "AWSConfigBucketDelivery",
         "Effect": "Allow",
         "Principal": {
           "Service": "config.amazonaws.com"
         },
         "Action": "s3:PutObject",
         "Resource": "arn:aws:s3:::targetBucketName/[optional] prefix/AWSLogs/sourceAccountID/Config/*",
         "Condition": { 
           "StringEquals": { 
             "s3:x-amz-acl": "bucket-owner-full-control",
             "AWS:SourceAccount": "sourceAccountID"
           }
         }
       }
     ]
   }
   ```
**Note**  
AWS Config is owned by AWS and does not belong specifically to one of your AWS accounts or linked accounts within your AWS Organization\. This means that when AWS Config is sending configuration items as the AWS Config service principal \(such as when the IAM role that you assigned when you set up AWS Config doesn’t have `WRITE` access to the bucket or when you setup AWS Config to use a service\-linked role\), the service won't work with organization ID or organization units based conditions\.
**Note**  
When granting permissions to your IAM role instead of AWS Config service principal name \(SPN\), ensure that your IAM role has `PutObjectACL` permission on cross\-account bucket to avoid insufficient permission error\.  See sample IAM role policy at [ IAM Role Policy for Amazon S3 Bucket](iamrole-permissions.md#iam-role-policies-S3-bucket)\.

1. Substitute the following values in the bucket policy:
   + *targetBucketName* – The name of the Amazon S3 bucket to which AWS Config will deliver configuration items\.
   + *\[optional\] prefix* – An optional addition to the Amazon S3 object key that helps create a folder\-like organization in the bucket\.
   + *sourceAccountID* – The ID of the account for which AWS Config will deliver configuration items to the target bucket\.

1. Choose **Save** and then **Close**\.

You can use the `AWS:SourceAccount` condition in the Amazon S3 bucket policy above to restrict the Config service principal to only interact with the Amazon S3 bucket when performing operations on behalf of specific accounts\. If you plan to set up AWS Config in many accounts from the same organization to deliver configuration items to a single Amazon S3 bucket, we recommend using IAM roles instead of service\-linked roles so you can use AWS Organizations conditions keys such as `AWS:PrincipalOrgID`\. For more information on managing access permissions for an IAM role to use with AWS Config, see [Permissions for the IAM Role Assigned to AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html)\. For more information about managing access permissions for AWS Organizations, see [Managing access permissions for your AWS organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html)\.

AWS Config also supports the `AWS:SourceArn` condition which restricts the Config service principal to only interact with the Amazon S3 bucket when performing operations on behalf of specific AWS Config delivery channels\. When using the AWS Config service principal, the `AWS:SourceArn` property will always be set to `arn:aws:config:sourceRegion:sourceAccountID:*` where `sourceRegion` is the region of the delivery channel and `sourceAccountID` is the ID of the account containing the delivery channel\. For more information on AWS Config delivery channels, see [Managing the Delivery Channel](https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html)\. For example, add the following condition to restrict the Config service principal to interact with your Amazon S3 bucket only on behalf of a delivery channel in the `us-east-1` region in the account `123456789012`: `"ArnLike": {"AWS:SourceArn": "arn:aws:config:us-east-1:123456789012:*"}`\.