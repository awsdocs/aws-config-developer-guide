# s3\-bucket\-versioning\-enabled<a name="s3-bucket-versioning-enabled"></a>

Checks if versioning is enabled for your S3 buckets\. Optionally, the rule checks if MFA delete is enabled for your S3 buckets\.

**Identifier:** S3\_BUCKET\_VERSIONING\_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

isMfaDeleteEnabled \(Optional\)Type: String  
MFA delete is enabled for your S3 buckets\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d511c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.