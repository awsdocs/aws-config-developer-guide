# s3\-bucket\-ssl\-requests\-only<a name="s3-bucket-ssl-requests-only"></a>

Checks whether S3 buckets have policies that require requests to use Secure Socket Layer \(SSL\)\.

**Identifier:**S3\_BUCKET\_SSL\_REQUESTS\_ONLY

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

 None   

An example of a bucket policy that is **COMPLIANT** with the SSL AWS Config rule is as follows:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": [ 
          "123412341234" 
        ]
      },
      "Action": "s3:Get*",
      "Resource": "arn:aws:s3:::example-bucket/*"
    },
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "*",
      "Resource": "arn:aws:s3:::example-bucket/*",
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

An example of a bucket policy that is **NON\_COMPLIANT** with the SSL AWS Config rule is as follows:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": [ 
          "123412341234" 
        ]
      },
      "Action": "s3:Get*",
      "Resource": "arn:aws:s3:::example-bucket/*"
    },
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "*",
      "Resource": "arn:aws:s3:::example-bucket/private/*",
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

## AWS CloudFormation template<a name="w22aac11c29c17d305c23"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.