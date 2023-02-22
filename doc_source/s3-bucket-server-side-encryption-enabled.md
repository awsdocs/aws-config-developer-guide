# s3\-bucket\-server\-side\-encryption\-enabled<a name="s3-bucket-server-side-encryption-enabled"></a>

Checks if your Amazon S3 bucket either has the Amazon S3 default encryption enabled or that the Amazon S3 bucket policy explicitly denies `put-object` requests without server side encryption that uses AES\-256 or AWS Key Management Service\. The rule is NON\_COMPLIANT if your Amazon S3 bucket is not encrypted by default\.

**Identifier:** S3\_BUCKET\_SERVER\_SIDE\_ENCRYPTION\_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d507c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.