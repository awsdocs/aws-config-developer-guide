# eks\-secrets\-encrypted<a name="eks-secrets-encrypted"></a>

Checks if Amazon Elastic Kubernetes Service clusters are configured to have Kubernetes secrets encrypted using AWS Key Management Service \(KMS\) keys\.
+ This rule is COMPLIANT if an EKS cluster has an encryptionConfig with secrets as one of the resources\.
+ This rule is also COMPLIANT if the key used to encrypt EKS secrets matches with the parameter\.
+ This rule is NON\_COMPLIANT if an EKS cluster does not have an encryptionConfig or if the encryptionConfig resources do not include secrets\.
+ This rule is also NON\_COMPLIANT if the key used to encrypt EKS secrets does not match with the parameter\.

**Identifier:** EKS\_SECRETS\_ENCRYPTED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Europe \(Milan\), US West \(N\. California\), Africa \(Cape Town\) Region

**Parameters:**

kmsKeyArns \(Optional\)Type: CSV  
Comma separated list of Amazon Resource Name \(ARN\) of the KMS key that should be used for encrypted secrets in an EKS cluster\.

## AWS CloudFormation template<a name="w26aac11c31c17b7d147c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.