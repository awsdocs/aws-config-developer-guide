# sagemaker\-endpoint\-configuration\-kms\-key\-configured<a name="sagemaker-endpoint-configuration-kms-key-configured"></a>

Checks whether AWS Key Management Service \(KMS\) key is configured for an Amazon SageMaker endpoint configuration\. The rule is NON\_COMPLIANT if 'KmsKeyId' is not specified for the Amazon SageMaker endpoint configuration\. 

**Identifier:** SAGEMAKER\_ENDPOINT\_CONFIGURATION\_KMS\_KEY\_CONFIGURED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

kmsKeyArns \(Optional\)Type: String  
Comma\-separated list of specific AWS KMS key ARNs allowed for an Amazon SageMaker endpoint configuration\.

## AWS CloudFormation template<a name="w79aac11c32c17b9d515c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.