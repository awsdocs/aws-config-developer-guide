# cloudwatch\-log\-group\-encrypted<a name="cloudwatch-log-group-encrypted"></a>

Checks whether a log group in Amazon CloudWatch Logs is encrypted with a AWS Key Management Service \(KMS\) managed Customer Master Keys \(CMK\)\. The rule is NON\_COMPLIANT if no AWS KMS CMK is configured on the log groups\.

**Identifier:** CLOUDWATCH\_LOG\_GROUP\_ENCRYPTED

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions except China \(Beijing\) and China \(Ningxia\)

**Parameters:**

 KmsKeyId   
\(Optional\) Amazon Resource Name \(ARN\) of an AWS Key Management Service \(KMS\) key that is used to encrypt the CloudWatch Logs log group\.

## AWS CloudFormation template<a name="w22aac11c29c17c69c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.