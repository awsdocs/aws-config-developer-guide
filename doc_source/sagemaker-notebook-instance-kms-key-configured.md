# sagemaker\-notebook\-instance\-kms\-key\-configured<a name="sagemaker-notebook-instance-kms-key-configured"></a>

Check whether an AWS Key Management Service \(KMS\) key is configured for SageMaker notebook instance\. The rule is not NON\_COMPLIANT if `kmsKeyId` is not specified for the SageMaker notebook instance\. 

**Identifier:** SAGEMAKER\_NOTEBOOK\_INSTANCE\_KMS\_KEY\_CONFIGURED

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions except AWS GovCloud \(US\-East\), China \(Beijing\), China \(Ningxia\), Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 kmsKeyArns \(optional\)  
Comma\-separated list of allowed AWS KMS key IDs allowed for SageMaker notebook instance\.

## AWS CloudFormation template<a name="w22aac11c29c17d311c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.