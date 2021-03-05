# efs\-encrypted\-check<a name="efs-encrypted-check"></a>

Checks whether Amazon EFS are configured to encrypt file data using AWS KMS\. The rule is NON\_COMPLIANT if the Encrypted key is set to False on DescribeFileSystems or, if specified, `KmsKeyId` key on DescribeFileSystems is not matching `KmsKeyId` parameter\. 

**Identifier:** EFS\_ENCRYPTED\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

KmsKeyId \(Optional\)Type: String  
Amazon Resource Name \(ARN\) of the KMS key that is used to encrypt the EFS file system\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d139c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.