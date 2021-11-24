# Permissions for the KMS Key<a name="s3-kms-key-policy"></a>

Create a policy for an Amazon S3 KMS Key that allows you to use KMS\-based encryption on objects delivered by AWS Config for S3 bucket delivery\.

**Contents**
+ [Required Permissions for the KMS Key When Using IAM Roles \(S3 Bucket Delivery\)](#required-permissions-s3-kms-key-using-iam-role)
+ [Required Permissions for the KMS Key When Using Service\-Linked Roles \(S3 Bucket Delivery\)](#required-permissions-s3-kms-key-using-servicelinkedrole)

## Required Permissions for the KMS Key When Using IAM Roles \(S3 Bucket Delivery\)<a name="required-permissions-s3-kms-key-using-iam-role"></a>

If you set up AWS Config using an IAM role, you can attach the follow permission policy to the KMS Key:

```
{
    "Id": "Policy_ID",
    "Statement": [
        {
            "Sid": "AWSConfigKMSPolicy",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Effect": "Allow",
            "Resource": "*myKMSKeyARN*",
            "Principal": {
                "AWS": [
                    "account-id1",
                    "account-id2",
                    "account-id3"
                ]
            }
        }
    ]
}
```

**Note**  
If the IAM role, Amazon S3 bucket policy, or AWS KMS key do not provide appropriate access to AWS Config, then AWS Config’s attempt to send configuration information to the Amazon S3 bucket will fail\. In this event, AWS Config sends the information again, this time as the AWS Config service principal\. For this case, you must attach a permission policy, mentioned below, to the AWS KMS key to grant AWS Config access to use the key when delivering information to the Amazon S3 bucket\. 

## Required Permissions for the KMS Key When Using Service\-Linked Roles \(S3 Bucket Delivery\)<a name="required-permissions-s3-kms-key-using-servicelinkedrole"></a>

If you set up AWS Config using a service\-linked role, you need to attach the following permission policy to the KMS Key\.

```
{
    "Id": "Policy_ID",
    "Statement": [
        {
            "Sid": "AWSConfigKMSPolicy",
            "Effect": "Allow",
            "Principal": {
                "Service": "config.amazonaws.com"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "myKMSKeyARN",
            "Condition": { 
                "StringEquals": {
                    "AWS:SourceAccount": "sourceAccountID"
                }
            }
        }
    ]
}
```

Substitute the following values in the key policy:
+ *myKMSKeyARN* – The ARN of the AWS KMS key used to encrypt data in the Amazon S3 bucket that AWS Config will deliver configuration items to\.
+ *sourceAccountID* – The ID of the account for which AWS Config will deliver configuration items to\.

You can use the `AWS:SourceAccount` condition in the AWS KMS key policy above to restrict the Config service principal to only interact with the AWS KMS key when performing operations on behalf of specific accounts\.

AWS Config also supports the `AWS:SourceArn` condition which restricts the Config service principal to only interact with the Amazon S3 bucket when performing operations on behalf of specific AWS Config delivery channels\. When using the AWS Config service principal, the `AWS:SourceArn` property will always be set to `arn:aws:config:sourceRegion:sourceAccountID:*` where `sourceRegion` is the region of the delivery channel and `sourceAccountID` is the ID of the account containing the delivery channel\. For more information on AWS Config delivery channels, see [Managing the Delivery Channel](https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html)\. For example, add the following condition to restrict the Config service principal to interact with your Amazon S3 bucket only on behalf of a delivery channel in the `us-east-1` region in the account `123456789012`: `"ArnLike": {"AWS:SourceArn": "arn:aws:config:us-east-1:123456789012:*"}`\.