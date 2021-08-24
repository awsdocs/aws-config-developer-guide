# s3\-default\-encryption\-kms<a name="s3-default-encryption-kms"></a>

Checks whether the Amazon S3 buckets are encrypted with AWS Key Management Service\(AWS KMS\)\. The rule is NON\_COMPLIANT if the Amazon S3 bucket is not encrypted with AWS KMS key\. 

**Identifier:** S3\_DEFAULT\_ENCRYPTION\_KMS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\) Region

**Parameters:**

kmsKeyArns \(Optional\)Type: CSV  
Comma separated list of AWS KMS key ARNs allowed for encrypting Amazon S3 Buckets\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d359c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.