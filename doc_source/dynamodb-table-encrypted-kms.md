# dynamodb\-table\-encrypted\-kms<a name="dynamodb-table-encrypted-kms"></a>

Checks whether Amazon DynamoDB table is encrypted with AWS Key Management Service \(KMS\)\. The rule is NON\_COMPLIANT if DynamoDB table is not encrypted with AWS KMS\. The rule is also NON\_COMPLIANT if the encrypted AWS KMS key is not present in `kmsKeyArns` input parameter\.

**Identifier:** DYNAMODB\_TABLE\_ENCRYPTED\_KMS

**Trigger type:** Configuration changes

**Parameters:**

 kmsKeyArns \(Optional\)  
Comma separated list of AWS KMS Key ARN list\.

## AWS CloudFormation template<a name="w22aac11c29c17c99c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.