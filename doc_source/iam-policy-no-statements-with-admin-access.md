# iam\-policy\-no\-statements\-with\-admin\-access<a name="iam-policy-no-statements-with-admin-access"></a>

Checks the IAM policies that you create for Allow statements that grant permissions to all actions on all resources\. The rule is NON\_COMPLIANT if any policy statement includes "Effect": "Allow" with "Action": "\*" over "Resource": "\*"\.

The following policy is NON\_COMPLIANT:

```
"Statement": [
{
"Sid": "VisualEditor",
"Effect": "Allow",
"Action": "*",
"Resource": "*"
}
```

The following policy is COMPLIANT:

```
"Statement": [
{
"Sid": "VisualEditor",
"Effect": "Allow",
"Action": "service:*",
"Resource": "*"
}
```

This rule checks only the IAM policies that you create\. It does not check IAM Managed Policies\. When you enable the rule, this rule checks all of the customer managed policies in your account, and all new policies that you create\.

**Identifier:** IAM\_POLICY\_NO\_STATEMENTS\_WITH\_ADMIN\_ACCESS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

 None  

## AWS CloudFormation template<a name="w22aac11c29c17d205c27"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.