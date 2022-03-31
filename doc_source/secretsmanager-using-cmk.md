# secretsmanager\-using\-cmk<a name="secretsmanager-using-cmk"></a>

Checks if all secrets in AWS Secrets Manager are encrypted using the AWS managed key \(`aws/secretsmanager`\) or a customer managed key that you created in AWS Key Management Service \(AWS KMS\)\. This rule is COMPLIANT if a secret is encrypted using a customer managed key\. This rule is NON\_COMPLIANT if a secret is encrypted using `aws/secretsmanager`\. 

**Identifier:** SECRETSMANAGER\_USING\_CMK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

kmsKeyArns \(Optional\)Type: CSV  
Comma\-separated list of KMS key Amazon Resource Names \(ARNs\) to check if the keys are used in the encryption\.

## AWS CloudFormation template<a name="w76aac11c31c17b7d477c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.