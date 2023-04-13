# dynamodb\-table\-encrypted\-kms<a name="dynamodb-table-encrypted-kms"></a>

Checks if Amazon DynamoDB table is encrypted with AWS Key Management Service \(KMS\)\. The rule is NON\_COMPLIANT if Amazon DynamoDB table is not encrypted with AWS KMS\. The rule is also NON\_COMPLIANT if the encrypted AWS KMS key is not present in `kmsKeyArns` input parameter\.

**Identifier:** DYNAMODB\_TABLE\_ENCRYPTED\_KMS

**Resource Types:** AWS::DynamoDB::Table

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

kmsKeyArns \(Optional\)Type: CSV  
Comma separated list of AWS KMS key ARNs allowed for encrypting Amazon DynamoDB Tables\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d175c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.