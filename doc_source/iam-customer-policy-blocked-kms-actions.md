# iam\-customer\-policy\-blocked\-kms\-actions<a name="iam-customer-policy-blocked-kms-actions"></a>

Checks that the managed AWS Identity and Access Management policies that you create do not allow blocked actions on all AWS AWS KMS keys\. The rule is NON\_COMPLIANT if any blocked action is allowed on all AWS AWS KMS keys by the managed IAM policy\. 

**Identifier:** IAM\_CUSTOMER\_POLICY\_BLOCKED\_KMS\_ACTIONS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

blockedActionsPatternsType: CSV  
Comma\-separated list of blocked KMS action patterns, for example, kms:\*, kms:Decrypt, kms:ReEncrypt\*\.

## AWS CloudFormation template<a name="w22aac11c29c17c11c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.