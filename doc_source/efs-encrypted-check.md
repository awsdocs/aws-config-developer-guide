# efs\-encrypted\-check<a name="efs-encrypted-check"></a>

Checks if Amazon Elastic File System \(Amazon EFS\) is configured to encrypt the file data using AWS Key Management Service \(AWS KMS\)\. The rule is NON\_COMPLIANT if the encrypted key is set to false on `DescribeFileSystems` or if the `KmsKeyId` key on `DescribeFileSystems` does not match the `KmsKeyId` parameter\.

**Identifier:** EFS\_ENCRYPTED\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

KmsKeyId \(Optional\)Type: String  
Amazon Resource Name \(ARN\) of the KMS key that is used to encrypt the EFS file system\.

## AWS CloudFormation template<a name="w76aac11c31c17b7d223c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.