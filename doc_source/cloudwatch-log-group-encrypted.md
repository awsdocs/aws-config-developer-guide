# cloudwatch\-log\-group\-encrypted<a name="cloudwatch-log-group-encrypted"></a>

Checks whether a log group in Amazon CloudWatch Logs is encrypted\. The rule is NON\_COMPLIANT if CloudWatch Logs has a log group without encryption enabled\.

**Identifier:** CLOUDWATCH\_LOG\_GROUP\_ENCRYPTED

**Trigger type:** Periodic

**Parameters:**

 KmsKeyId   
\(Optional\) Amazon Resource Name \(ARN\) of an AWS Key Management Service \(KMS\) key that is used to encrypt the CloudWatch Logs log group\.

## AWS CloudFormation template<a name="w4aac13c29c17c73c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.