# secretsmanager\-using\-cmk<a name="secretsmanager-using-cmk"></a>

Checks if all secrets in AWS Secrets Manager are encrypted using an AWS Key Management Service \(AWS KMS\) customer master key \(CMK\)\. This rule is COMPLIANT if a secret is encrypted using an AWS KMS CMK\. This rule is NON\_COMPLIANT if a secret is encrypted using the default AWS KMS key\.

**Identifier:** SECRETSMANAGER\_USING\_CMK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

kmsKeyArns \(Optional\)Type: CSV  
Comma\-separated list of KMS key Amazon Resource Names \(ARNs\) to check if the keys are used in the encryption\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d333c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.