# redshift\-cluster\-kms\-enabled<a name="redshift-cluster-kms-enabled"></a>

Checks if Amazon Redshift clusters are using a specified AWS Key Management Service \(AWS KMS\) key for encryption\. The rule is COMPLIANT if encryption is enabled and the cluster is encrypted with the key provided in the `kmsKeyArn` parameter\. The rule is NON\_COMPLIANT if the cluster is not encrypted or encrypted with another key\.

**Identifier:** REDSHIFT\_CLUSTER\_KMS\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Osaka\) Region

**Parameters:**

kmsKeyArns \(Optional\)Type: CSV  
Comma\-separated list of AWS KMS key Amazon Resource Names \(ARNs\) used in Amazon Redshift clusters for encryption\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d291c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.