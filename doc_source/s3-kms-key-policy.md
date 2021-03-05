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
            "Resource": "myKMSKeyARN"
        }
    ]
}
```