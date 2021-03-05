# eks\-secrets\-encrypted<a name="eks-secrets-encrypted"></a>

Checks whether Amazon Elastic Kubernetes Service clusters are configured to have Kubernetes secrets encrypted using AWS Key Management Service \(KMS\) keys\. This rule is NON\_COMPLIANT if an EKS cluster does not have an encryptionConfig\. 

**Identifier:** EKS\_SECRETS\_ENCRYPTED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Europe \(Milan\), US West \(N\. California\), Africa \(Cape Town\) Region

**Parameters:**

kmsKeyArns \(Optional\)Type: CSV  
Comma separated list of Amazon Resource Name \(ARN\) of the KMS key that should be used for encrypted secrets in an EKS cluster\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d147c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.