# s3\-bucket\-server\-side\-encryption\-enabled<a name="s3-bucket-server-side-encryption-enabled"></a>

Checks if your Amazon S3 bucket either has the Amazon S3 default encryption enabled or that the Amazon S3 bucket policy explicitly denies `put-object` requests without server side encryption that uses AES\-256 or AWS Key Management Service\. The rule is NON\_COMPLIANT if your Amazon S3 bucket is not encrypted by default\.

**Identifier:** S3\_BUCKET\_SERVER\_SIDE\_ENCRYPTION\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template<a name="w29aac11c33c17b7d353c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.