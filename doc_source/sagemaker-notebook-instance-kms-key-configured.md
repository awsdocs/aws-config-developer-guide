# sagemaker\-notebook\-instance\-kms\-key\-configured<a name="sagemaker-notebook-instance-kms-key-configured"></a>

Check whether an AWS Key Management Service \(KMS\) key is configured for an Amazon SageMaker notebook instance\. The rule is NON\_COMPLIANT if 'KmsKeyId' is not specified for the Amazon SageMaker notebook instance\. 

**Identifier:** SAGEMAKER\_NOTEBOOK\_INSTANCE\_KMS\_KEY\_CONFIGURED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

kmsKeyArns \(Optional\)Type: String  
Comma\-separated list of AWS KMS key ARNs allowed for an Amazon SageMaker notebook instance\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d363c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.