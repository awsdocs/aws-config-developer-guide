# Permissions for the Amazon S3 Bucket<a name="s3-bucket-policy"></a>

By default, all Amazon S3 buckets and objects are private\. Only the resource owner which is the AWS account that created the bucket can access that bucket and any objects it contains\. The resource owner can, however, choose to grant access permissions to other resources and users\. One way to do this is to write an access policy\. 

If AWS Config creates an Amazon S3 bucket for you automatically \(for example, if you use AWS Config console to set up your delivery channel\), these permissions are automatically added to Amazon S3 bucket\. However, if you specify an existing Amazon S3 bucket, you must ensure that the S3 bucket has the correct permissions\.

**Contents**
+ [Required Permissions for the Amazon S3 Bucket When Using IAM Roles](#required-permissions-in-another-account)
+ [Required Permissions for the Amazon S3 Bucket When Using Service\-Linked Roles](#required-permissions-using-servicelinkedrole)
+ [Granting AWS Config access to the Amazon S3 Bucket](#granting-access-in-another-account)

## Required Permissions for the Amazon S3 Bucket When Using IAM Roles<a name="required-permissions-in-another-account"></a>

When AWS Config sends configuration information \(history files and snapshots\) to Amazon S3 bucket in your account, it assumes the IAM role that you assigned when you set up AWS Config\. When AWS Config sends configuration information to an Amazon S3 bucket in another account, it first attempts to use the IAM role, but this attempt fails if the access policy for the bucket does not grant `WRITE` access to the IAM role\. In this event, AWS Config sends the information again, this time as the AWS Config service principal\. Before the delivery can succeed, the access policy must grant `WRITE` access to the `config.amazonaws.com` principal name\. AWS Config is then the owner of the objects it delivers to the S3 bucket\. You must attach an access policy, mentioned in step 6 below to the Amazon S3 bucket in another account to grant AWS Config access to the Amazon S3 bucket\.

Before AWS Config can deliver logs to your Amazon S3 bucket AWS Config checks whether the bucket exists and in which AWS region the bucket is located\. AWS Config attempts to call Amazon S3 [HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RESTBucketHEAD.html) API to check whether the bucket exists and to get the bucket region\. If permissions are not provided to locate the bucket when the location check is performed, you see `AccessDenied` error in AWS CloudTrail logs\. However, the log delivery to your Amazon S3 bucket succeeds if you do not provide bucket location permissions\.

## Required Permissions for the Amazon S3 Bucket When Using Service\-Linked Roles<a name="required-permissions-using-servicelinkedrole"></a>

If you set up AWS Config using a service\-linked role, you need to attach an access policy, mentioned in step 6 below to the Amazon S3 bucket in your own account or another account to grant AWS Config access to the Amazon S3 bucket\.

## Granting AWS Config access to the Amazon S3 Bucket<a name="granting-access-in-another-account"></a>

Follow these steps to add an access policy to the Amazon S3 bucket in your own account or another account\. The access policy allows AWS Config to send configuration information to the Amazon S3 bucket\.

1. Sign in to the AWS Management Console using the account that has the S3 bucket\.

1. Open the Amazon S3 console at [https://console\.aws\.amazon\.com/s3/](https://console.aws.amazon.com/s3/)\.

1. Select the bucket that you want AWS Config to use to deliver configuration items, and then choose **Properties**\. 

1. Choose **Permissions**\.

1. Choose **Edit Bucket Policy**\.

1. Copy the following policy into the **Bucket Policy Editor** window:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AWSConfigBucketPermissionsCheck",
         "Effect": "Allow",
         "Principal": {
           "Service": [
            "config.amazonaws.com"
           ]
         },
         "Action": "s3:GetBucketAcl",
         "Resource": "arn:aws:s3:::targetBucketName"
       },
       {
         "Sid": "AWSConfigBucketExistenceCheck",
         "Effect": "Allow",
         "Principal": {
           "Service": [
             "config.amazonaws.com"
           ]
         },
         "Action": "s3:ListBucket",
         "Resource": "arn:aws:s3:::targetBucketName"
       },
       {
         "Sid": "AWSConfigBucketDelivery",
         "Effect": "Allow",
         "Principal": {
           "Service": [
            "config.amazonaws.com"    
           ]
         },
         "Action": "s3:PutObject",
         "Resource": "arn:aws:s3:::targetBucketName/[optional] prefix/AWSLogs/sourceAccountID-WithoutHyphens/Config/*",
         "Condition": { 
           "StringEquals": { 
             "s3:x-amz-acl": "bucket-owner-full-control" 
           }
         }
       }
     ]
   }
   ```

1. Substitute the following values in the bucket policy:
   + *targetBucketName* – The name of the Amazon S3 bucket to which AWS Config will deliver configuration items\.
   + *\[optional\] prefix* – An optional addition to the Amazon S3 object key that helps create a folder\-like organization in the bucket\.
   + *sourceAccountID\-WithoutHyphens* – The ID of the account for which AWS Config will deliver configuration items to the target bucket\.

1. Choose **Save** and then **Close**\.