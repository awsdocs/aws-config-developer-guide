# sagemaker\-endpoint\-configuration\-kms\-key\-configured<a name="sagemaker-endpoint-configuration-kms-key-configured"></a>

Checks whether AWS Key Management Service \(KMS\) key is configured for an Amazon SageMaker endpoint configuration\. The rule is NON\_COMPLIANT if `KmsKeyId` is not specified for the Amazon SageMaker endpoint configuration\.

**Identifier:** SAGEMAKER\_ENDPOINT\_CONFIGURATION\_KMS\_KEY\_CONFIGURED

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions except AWS GovCloud \(US\-East\), China \(Beijing\), China \(Ningxia\), Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

kmsKeyArns  
\(Optional\) Comma\-separated list of specific AWS KMS key ARNs allowed for an Amazon SageMaker endpoint configuration\. 

## AWS CloudFormation template<a name="w22aac11c29c17d309c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.