# eks\-secrets\-encrypted<a name="eks-secrets-encrypted"></a>

Checks if Amazon Elastic Kubernetes Service clusters are configured to have Kubernetes secrets encrypted using AWS Key Management Service \(KMS\) keys\.
+ This rule is COMPLIANT if an EKS cluster has an encryptionConfig with secrets as one of the resources\.
+ This rule is also COMPLIANT if the key used to encrypt EKS secrets matches with the parameter\.
+ This rule is NON\_COMPLIANT if an EKS cluster does not have an encryptionConfig or if the encryptionConfig resources do not include secrets\.
+ This rule is also NON\_COMPLIANT if the key used to encrypt EKS secrets does not match with the parameter\.

**Identifier:** EKS\_SECRETS\_ENCRYPTED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), US West \(N\. California\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

kmsKeyArns \(Optional\)Type: CSV  
Comma separated list of Amazon Resource Name \(ARN\) of the KMS key that should be used for encrypted secrets in an EKS cluster\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d277c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.