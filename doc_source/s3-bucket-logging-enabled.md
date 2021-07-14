# s3\-bucket\-logging\-enabled<a name="s3-bucket-logging-enabled"></a>

Checks whether logging is enabled for your S3 buckets\. 

**Identifier:** S3\_BUCKET\_LOGGING\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

targetBucket \(Optional\)Type: String  
Target S3 bucket for storing server access logs\.

targetPrefix \(Optional\)Type: String  
Prefix of the S3 bucket for storing server access logs\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d319c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.