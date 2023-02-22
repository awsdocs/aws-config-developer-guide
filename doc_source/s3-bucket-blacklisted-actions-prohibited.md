# s3\-bucket\-blacklisted\-actions\-prohibited<a name="s3-bucket-blacklisted-actions-prohibited"></a>

Checks if an Amazon Simple Storage Service \(Amazon S3\) bucket policy does not allow blocklisted bucket\-level and object\-level actions on resources in the bucket for principals from other AWS accounts\. For example, the rule checks that the Amazon S3 bucket policy does not allow another AWS account to perform any `s3:GetBucket*` actions and `s3:DeleteObject` on any object in the bucket\. The rule is NON\_COMPLIANT if any blocklisted actions are allowed by the Amazon S3 bucket policy\.

**Note**  
The rule will only check for entities in the Principal property and does not take into account any conditionals under the Condition property in a policy

**Identifier:** S3\_BUCKET\_BLACKLISTED\_ACTIONS\_PROHIBITED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

blacklistedActionPatternType: CSV  
Comma\-separated list of blacklisted action patterns, for example, s3:GetBucket\* and s3:DeleteObject\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d489c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.