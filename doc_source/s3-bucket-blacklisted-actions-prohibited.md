# s3\-bucket\-blacklisted\-actions\-prohibited<a name="s3-bucket-blacklisted-actions-prohibited"></a>

Checks that the S3 bucket policy does not allow blacklisted bucket\-level and object\-level actions for principals from other AWS Accounts\. The rule is non\-compliant if any blacklisted actions are allowed by the S3 bucket policy\. 

**Identifier:** S3\_BUCKET\_BLACKLISTED\_ACTIONS\_PROHIBITED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

blacklistedActionPatternType: CSV  
Comma\-separated list of blacklisted action patterns, for example, s3:GetBucket\* and s3:DeleteObject\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d293c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.