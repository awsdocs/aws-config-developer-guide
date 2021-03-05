# dynamodb\-table\-encrypted\-kms<a name="dynamodb-table-encrypted-kms"></a>

Checks whether Amazon DynamoDB table is encrypted with AWS Key Management Service \(KMS\)\. The rule is NON\_COMPLIANT if Amazon DynamoDB table is not encrypted with AWS KMS\. 

**Identifier:** DYNAMODB\_TABLE\_ENCRYPTED\_KMS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

kmsKeyArns \(Optional\)Type: CSV  
Comma separated list of AWS KMS key ARNs allowed for encrypting Amazon DynamoDB Tables\.

## AWS CloudFormation template<a name="w24aac11c29c17b7c99c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.