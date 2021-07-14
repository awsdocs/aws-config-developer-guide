# iam\-user\-no\-policies\-check<a name="iam-user-no-policies-check"></a>

Checks that none of your IAM users have policies attached\. IAM users must inherit permissions from IAM groups or roles\. The rule is NONCOMPLIANT if there is at least one IAM user with policies attached\.

**Identifier:** IAM\_USER\_NO\_POLICIES\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template<a name="w29aac11c33c17b7d231c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.