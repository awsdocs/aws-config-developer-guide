# Permissions for the IAM Role Assigned to AWS Config<a name="iamrole-permissions"></a>

An AWS Identity and Access Management \(IAM\) role lets you define a set of permissions\. AWS Config assumes the role that you assign to it to write to your S3 bucket, publish to your SNS topic, and to make `Describe` or `List` API requests to get configuration details for your AWS resources\. For more information on IAM roles, see [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html) in the *IAM User Guide*\.

When you use the AWS Config console to create or update an IAM role, AWS Config automatically attaches the required permissions for you\. For more information, see [Setting Up AWS Config with the Console](gs-console.md)\.

**Contents**
+ [Creating IAM Role Policies](#iam-role-policies)
  + [Adding an IAM Trust Policy to your Role](#iam-trust-policy)
  + [IAM Role Policy for Amazon S3 Bucket](#iam-role-policies-S3-bucket)
  + [IAM Role Policy for KMS Key](#iam-role-policies-S3-kms-key)
  + [IAM Role Policy for Amazon SNS Topic](#iam-role-policies-sns-topic)
  + [IAM Role Policy for Getting Configuration Details](#iam-role-policies-describe-apis)
+ [Managing Permissions for S3 Bucket Recording](#troubleshooting-recording-s3-bucket-policy)

## Creating IAM Role Policies<a name="iam-role-policies"></a>

When you use the AWS Config console to create an IAM role, AWS Config automatically attaches the required permissions to the role for you\. 

If you are using the AWS CLI to set up AWS Config or you are updating an existing IAM role, you must manually update the policy to allow AWS Config to access your S3 bucket, publish to your SNS topic, and get configuration details about your resources\.

### Adding an IAM Trust Policy to your Role<a name="iam-trust-policy"></a>

You can create an IAM trust policy that enables AWS Config to assume a role and use it to track your resources\. For more information about trust policies, see [Assuming a Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-assume-role.html) in the* IAM User Guide*\.

The following is an example trust policy for AWS Config roles:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "config.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### IAM Role Policy for Amazon S3 Bucket<a name="iam-role-policies-S3-bucket"></a>

The following example policy grants AWS Config permissions to access your Amazon S3 bucket:

```
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Action":[
        "s3:PutObject",
        "s3:PutObjectAcl"
      ],
      "Resource":[
        "arn:aws:s3:::myBucketName/prefix/AWSLogs/myAccountID/*"
      ],
      "Condition":{
        "StringLike":{
          "s3:x-amz-acl":"bucket-owner-full-control"
        }
      }
    },
    {
      "Effect":"Allow",
      "Action":[
        "s3:GetBucketAcl"
      ],
      "Resource":"arn:aws:s3:::myBucketName"
    }
  ]
}
```

### IAM Role Policy for KMS Key<a name="iam-role-policies-S3-kms-key"></a>

The following example policy grants AWS Config permissions to use KMS\-based encryption on new objects for S3 bucket delivery:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "myKMSKeyARN"
        }
    ]
}
```

### IAM Role Policy for Amazon SNS Topic<a name="iam-role-policies-sns-topic"></a>

The following example policy grants AWS Config permissions to access your SNS topic:

```
{
  "Version": "2012-10-17",
  "Statement": 
   [
     {
      "Effect":"Allow",
      "Action":"sns:Publish",
      "Resource":"mySNStopicARN"
     }
    ]
}
```

If your SNS topic is encrypted for additional setup instructions, see [Configuring AWS KMS Permissions](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sns-what-permissions-for-sse) in the *Amazon Simple Notification Service Developer Guide*\.

### IAM Role Policy for Getting Configuration Details<a name="iam-role-policies-describe-apis"></a>

To record your AWS resource configurations, AWS Config requires IAM permissions to get the configuration details about your resources\. 

Use the AWS managed policy **AWS\_ConfigRole** and attach it to the IAM role that you assign to AWS Config\. AWS updates this policy each time AWS Config adds support for an AWS resource type, which means AWS Config will continue to have the required permissions to get configuration details as long as the role has this managed policy attached\.

If you create or update a role with the console, AWS Config attaches the **AWS\_ConfigRole** for you\. 

If you use the AWS CLI, use the `attach-role-policy` command and specify the Amazon Resource Name \(ARN\) for **AWS\_ConfigRole**:

```
$ aws iam attach-role-policy --role-name myConfigRole --policy-arn arn:aws:iam::aws:policy/service-role/AWS_ConfigRole
```

## Managing Permissions for S3 Bucket Recording<a name="troubleshooting-recording-s3-bucket-policy"></a>

AWS Config records and delivers notifications when an S3 bucket is created, updated, or deleted\.

It's recommended that you use either the `AWSServiceRoleForConfig` \(see [Using Service\-Linked Roles for AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/using-service-linked-roles.html)\) or a custom IAM role utilizing the `AWS_ConfigRole` managed policy\. For more information on best practices for configuration recording, see [AWS Config Best Practices](https://aws.amazon.com/blogs/mt/aws-config-best-practices/)\.

If you need to manage object\-level permissions for your bucket recording, make sure in the S3 bucket policy to provide `config.amazonaws.com` \(the AWS Config service principal name\) access to all S3 related permissions from the `AWS_ConfigRole` managed policy\. For more information, see [Permissions for the Amazon S3 Bucket](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html)\.