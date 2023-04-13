# kms\-cmk\-not\-scheduled\-for\-deletion<a name="kms-cmk-not-scheduled-for-deletion"></a>

Checks if AWS KMS keys are not scheduled for deletion in AWS Key Management Service \(AWS KMS\)\. The rule is NON\_COMPLAINT if KMS keys are scheduled for deletion\. 

**Identifier:** KMS\_CMK\_NOT\_SCHEDULED\_FOR\_DELETION

**Resource Types:** AWS::KMS::Key

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

kmsKeyIds \(Optional\)Type: String  
\(Optional\) Comma\-separated list of specific customer managed key IDs not to be scheduled for deletion\. If you do not specify any keys, the rule checks all the keys\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d395c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.