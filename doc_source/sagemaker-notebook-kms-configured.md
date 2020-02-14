# sagemaker\-notebook\-kms\-configured<a name="sagemaker-notebook-kms-configured"></a>

Check whether an AWS Key Management Service \(KMS\) key is configured for Amazon SageMaker notebook instance\. The rule is not NON\_COMPLIANT if `kmsKeyId` is not specified for the Amazon SageMaker notebook instance\. 

**Identifier:** SAGEMAKER\_NOTEBOOK\_INSTANCE\_KMS\_KEY\_CONFIGURED

**Trigger type:** Periodic

**AWS Regions:** All supported AWS regions except AWS GovCloud \(US\-Gov\-East\), China \(Beijing\), and China \(Ningxia\)

**Parameters:**

 keyArns \(optional\)  
Comma\-separated list of allowed AWS KMS key IDs allowed for Amazon SageMaker notebook instance\.

## AWS CloudFormation template<a name="w4aac13c29c17d261c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.