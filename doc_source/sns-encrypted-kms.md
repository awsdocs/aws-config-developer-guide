# sns\-encrypted\-kms<a name="sns-encrypted-kms"></a>

Checks if Amazon SNS topic is encrypted with AWS Key Management Service \(AWS KMS\)\. The rule is NON\_COMPLIANT if the Amazon SNS topic is not encrypted with AWS KMS\. The rule is also NON\_COMPLIANT when encrypted KMS key is not present in `kmsKeyIds` input parameter\.

**Identifier:** SNS\_ENCRYPTED\_KMS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\) Region

**Parameters:**

kmsKeyIds \(Optional\)Type: CSV  
Comma separated list of AWS KMS key ARNs allowed for encrypting Amazon SNS Topic\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d345c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.