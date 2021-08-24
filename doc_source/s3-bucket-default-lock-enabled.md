# s3\-bucket\-default\-lock\-enabled<a name="s3-bucket-default-lock-enabled"></a>

Checks whether Amazon S3 bucket has lock enabled, by default\. The rule is NON\_COMPLIANT if the lock is not enabled\. 

**Identifier:** S3\_BUCKET\_DEFAULT\_LOCK\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\) Region

**Parameters:**

mode \(Optional\)Type: String  
mode: \(optional\): A mode parameter with valid values of GOVERNANCE or COMPLIANCE\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d337c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.