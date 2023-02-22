# sns\-encrypted\-kms<a name="sns-encrypted-kms"></a>

Checks if Amazon SNS topic is encrypted with AWS Key Management Service \(AWS KMS\)\. The rule is NON\_COMPLIANT if the Amazon SNS topic is not encrypted with AWS KMS\. The rule is also NON\_COMPLIANT when encrypted KMS key is not present in `kmsKeyIds` input parameter\.

**Identifier:** SNS\_ENCRYPTED\_KMS

**Resource Types:** AWS::SNS::Topic

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

kmsKeyIds \(Optional\)Type: CSV  
Comma separated list of AWS KMS key ARNs allowed for encrypting Amazon SNS Topic\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d555c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.