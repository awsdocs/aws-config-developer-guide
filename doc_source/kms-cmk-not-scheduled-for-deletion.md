# kms\-cmk\-not\-scheduled\-for\-deletion<a name="kms-cmk-not-scheduled-for-deletion"></a>

Checks whether customer master keys \(CMKs\) are not scheduled for deletion in AWS Key Management Service \(KMS\)\. The rule is NON\_COMPLIANT if CMKs are scheduled for deletion\. 

**Identifier:** KMS\_CMK\_NOT\_SCHEDULED\_FOR\_DELETION

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 kmsKeyIds  
Comma\-separated list of specific customer managed key IDs not to be scheduled for deletion\. If you do not specify any keys, the rule checks all the keys\.

## AWS CloudFormation template<a name="w22aac11c29c17d221c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.