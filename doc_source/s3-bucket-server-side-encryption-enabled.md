# s3\-bucket\-server\-side\-encryption\-enabled<a name="s3-bucket-server-side-encryption-enabled"></a>

Checks that your Amazon S3 bucket either has Amazon S3 default encryption enabled or that the S3 bucket policy explicitly denies `put-object` requests without server side encryption that uses AES\-256 or AWS Key Management Service\.  

**Identifier:** S3\_BUCKET\_SERVER\_SIDE\_ENCRYPTION\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

 None  

## AWS CloudFormation template<a name="w22aac11c29c17d303c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.