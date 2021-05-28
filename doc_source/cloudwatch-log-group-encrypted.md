# cloudwatch\-log\-group\-encrypted<a name="cloudwatch-log-group-encrypted"></a>

Checks if a log group in Amazon CloudWatch Logs is encrypted with a AWS Key Management Service \(KMS\) managed Customer Master Keys \(CMK\)\. The rule is NON\_COMPLIANT if no AWS KMS CMK is configured on the log groups\.

**Identifier:** CLOUDWATCH\_LOG\_GROUP\_ENCRYPTED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), Asia Pacific \(Osaka\) Region

**Parameters:**

KmsKeyId \(Optional\)Type: String  
Amazon Resource Name \(ARN\) of AWS Key Management Service \(KMS\) key that is used to encrypt the CloudWatch Logs log group\.

## AWS CloudFormation template<a name="w29aac11c33c17b7c65c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.