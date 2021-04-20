# iam\-inline\-policy\-blocked\-kms\-actions<a name="iam-inline-policy-blocked-kms-actions"></a>

Checks that the inline policies attached to your IAM users, roles, and groups do not allow blocked actions on all AWS Key Management Service \(KMS\) keys\. The rule is NON\_COMPLIANT if any blocked action is allowed on all KMS keys in an inline policy\. 

**Identifier:** IAM\_INLINE\_POLICY\_BLOCKED\_KMS\_ACTIONS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\) Region

**Parameters:**

blockedActionsPatternsType: CSV  
Comma\-separated list of blocked KMS action patterns, for example, kms:\*, kms:Decrypt, kms:ReEncrypt\*\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d207c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.