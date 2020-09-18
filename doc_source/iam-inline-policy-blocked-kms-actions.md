# iam\-inline\-policy\-blocked\-kms\-actions<a name="iam-inline-policy-blocked-kms-actions"></a>

Checks that the inline policies attached to your AWS Identity and Access Management users, roles, and groups do not allow blocked actions on all AWS Key Management Service keys\. The rule is NON\_COMPLIANT if any blocked action is allowed on all AWS KMS keys in an inline policy\.

**Identifier:** IAM\_INLINE\_POLICY\_BLOCKED\_KMS\_ACTIONS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

blockedActionsPatternsType: CSV  
Comma\-separated list of blocked KMS action patterns, for example, kms:\*, kms:Decrypt, kms:ReEncrypt\*\.

## AWS CloudFormation template<a name="w22aac11c29c17b9c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.