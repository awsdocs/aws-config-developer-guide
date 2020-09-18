# s3\-bucket\-policy\-not\-more\-permissive<a name="s3-bucket-policy-not-more-permissive"></a>

Verifies that your Amazon Simple Storage Service bucket policies do not allow other inter\-account permissions than the control Amazon S3 bucket policy that you provide\. 

**Note**  
If you provide an invalid parameter value, you will see the following error: Value for controlPolicy parameter must be an Amazon S3 bucket policy\. 

**Identifier:** S3\_BUCKET\_POLICY\_NOT\_MORE\_PERMISSIVE

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

 controlPolicy  
Amazon S3 bucket policy that defines an upper bound on the permissions of your S3 buckets\. The policy can be a maximum of 1024 characters long\.

An example of a control policy is as follows\.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Principal": {
        "AWS": "11112222333"
      },
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "*"
    },
    {
      "Principal": {
        "AWS": "44445556666"
      },
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": "*"
    }
  ]
}
```

The first Allow statement specifies that the AWS account ID `111122223333` can retrieve objects \(`s3:GetObject`\) on any resource \(\*\)\. The second Allow statement specifies that the AWS account ID `44445556666` can perform any s3 action `(s3:*)` on any resource \(\*\)\.

Examples of **NON\_COMPLIANT** bucket policies with the above control policy as an input parameter for the rule are as follows\. 

The following bucket policy is NON\_COMPLIANT because the bucket policy allows permissions for the IAM user, Alice, in the AWS account ID `888899998888`\. These permissions are implicitly denied by the control policy\.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Principal": {
        "AWS": [
          "arn:aws:iam::888899998888:user/Alice"
        ]
      },
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::example-bucket/*"
    }
  ]
}
```

The following bucket policy is NON\_COMPLIANT because the bucket policy allows the AWS account ID `11112222333` permissions to perform `s3:PutBucketPolicy` that is implicitly denied by the control policy\.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Principal": {
        "AWS": [
          "11112222333"
        ]
      },
      "Effect": "Allow",
      "Action": "s3:PutBucketPolicy",
      "Resource": "arn:aws:s3:::example-bucket"
    }
  ]
}
```

Examples of **COMPLIANT** bucket policies are as follows\.

The following bucket policy is COMPLIANT because the control policy allows principals from the AWS account ID `11112222333` to perform `s3:GetObject` on any object\.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Principal": {
        "AWS" : [
          "arn:aws:iam::11112222333:user/Bob"
        ]
      },
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::example-bucket/photos/*"
    }
  ]
}
```

The following bucket policy is COMPLIANT because the control policy allows a principal with the AWS account ID `444455556666` to perform any S3 action\.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Principal": {
        "AWS": [
          "44445556666"
        ]
      },
      "Effect": "Allow",
      "Action": "s3:*Configuration",
      "Resource": "arn:aws:s3:::example-bucket"
    }
  ]
}
```

## AWS CloudFormation template<a name="w22aac11c29c17d291c43"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.