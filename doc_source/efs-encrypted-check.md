# efs\-encrypted\-check<a name="efs-encrypted-check"></a>

Checks whether Amazon Elastic File System \(Amazon EFS\) is configured to encrypt the file data using AWS Key Management Service \(AWS KMS\)\. The rule is NON\_COMPLIANT if the encrypted key is set to false on `DescribeFileSystems` or if the `KmsKeyId` key on `DescribeFileSystems` does not match the `KmsKeyId` parameter\.

**Identifier:** EFS\_ENCRYPTED\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

KmsKeyId \(optional\)  
Amazon Resource Name \(ARN\) of the AWS KMS key that is used to encrypt the Amazon EFS file system\.

## AWS CloudFormation template<a name="w22aac11c29c17d141c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.