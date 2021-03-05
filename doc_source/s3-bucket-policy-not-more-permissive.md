# s3\-bucket\-policy\-not\-more\-permissive<a name="s3-bucket-policy-not-more-permissive"></a>

Verifies that your Amazon S3 bucket policies do not allow other inter\-account permissions than the control S3 bucket policy that you provide\. 

**Identifier:** S3\_BUCKET\_POLICY\_NOT\_MORE\_PERMISSIVE

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

controlPolicyType: String  
Amazon S3 bucket policy that defines an upper bound on the permissions of your S3 buckets\. The policy can be a maximum of 1024 characters long\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d303c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.