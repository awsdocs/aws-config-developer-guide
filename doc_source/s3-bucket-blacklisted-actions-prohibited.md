# s3\-bucket\-blacklisted\-actions\-prohibited<a name="s3-bucket-blacklisted-actions-prohibited"></a>

Checks if the Amazon Simple Storage Service bucket policy does not allow blacklisted bucket\-level and object\-level actions on resources in the bucket for principals from other AWS accounts\. For example, the rule checks that the Amazon S3 bucket policy does not allow another AWS account to perform any s3:GetBucket\* actions and s3:DeleteObject on any object in the bucket\. The rule is NON\_COMPLIANT if any blacklisted actions are allowed by the Amazon S3 bucket policy\.

**Identifier:** S3\_BUCKET\_BLACKLISTED\_ACTIONS\_PROHIBITED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

blacklistedActionPatternType: CSV  
Comma\-separated list of blacklisted action patterns, for example, s3:GetBucket\* and s3:DeleteObject\.

## AWS CloudFormation template<a name="w76aac11c31c17b7d433c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.