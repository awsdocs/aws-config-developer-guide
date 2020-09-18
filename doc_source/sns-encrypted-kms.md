# sns\-encrypted\-kms<a name="sns-encrypted-kms"></a>

Checks whether Amazon SNS topic is encrypted with AWS Key Management Service \(AWS KMS\)\. The rule is NON\_COMPLIANT if the Amazon SNS topic is not encrypted with AWS KMS\. The rule is also NON\_COMPLIANT when encrypted KMS key is not present in `kmsKeyIds` input parameter\. 

**Identifier:** SNS\_ENCRYPTED\_KMS

**Trigger type:** Configuration changes

**Parameters:**

 kmsKeyIds \(Optional\)  
Comma separated list of AWS KMS key ARN list\.

## AWS CloudFormation template<a name="w22aac11c29c17d285c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.