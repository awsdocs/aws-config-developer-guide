# sns\-encrypted\-kms<a name="sns-encrypted-kms"></a>

Checks whether Amazon SNS topic is encrypted with AWS Key Management Service \(AWS KMS\)\. The rule is NON\_COMPLIANT if the Amazon SNS topic is not encrypted with AWS KMS\. 

**Identifier:** SNS\_ENCRYPTED\_KMS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

kmsKeyIds \(Optional\)Type: CSV  
Comma separated list of AWS KMS key ARNs allowed for encrypting Amazon SNS Topic\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d343c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.