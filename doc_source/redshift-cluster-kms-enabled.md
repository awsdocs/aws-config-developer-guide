# redshift\-cluster\-kms\-enabled<a name="redshift-cluster-kms-enabled"></a>

This rule enables users to specify an AWS Key Management Service key to check if Amazon RedShift clusters are using a key for encryption\. 

**Identifier:** REDSHIFT\_CLUSTER\_KMS\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

kmsKeyArns \(Optional\)Type: CSV  
Comma seperated KMS Key Arns to check if these keys are used in the Amazon RedShift clusters for encryption\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d275c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.