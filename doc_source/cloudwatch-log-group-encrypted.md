# cloudwatch\-log\-group\-encrypted<a name="cloudwatch-log-group-encrypted"></a>

Checks if a log group in Amazon CloudWatch Logs is encrypted with an AWS Key Management Service \(KMS\) key\. The rule is NON\_COMPLIANT if no AWS KMS key is configured on the log groups\.

**Identifier:** CLOUDWATCH\_LOG\_GROUP\_ENCRYPTED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

KmsKeyId \(Optional\)Type: String  
Amazon Resource Name \(ARN\) of AWS Key Management Service \(KMS\) key that is used to encrypt the CloudWatch Logs log group\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d109c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.