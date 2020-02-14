# iam\-policy\-no\-statements\-with\-admin\-access<a name="iam-policy-no-statements-with-admin-access"></a>

Checks the IAM policies that you create, such as identity\-based or resource\-based policies, for Allow statements that grant permissions to all actions on all resources\. The rule is NON\_COMPLIANT if any policy statement includes "Effect": "Allow" with "Action": "\*" over "Resource": "\*"\. For example, the following statement is NON\_COMPLIANT:

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

**Parameters:**

 None  

## AWS CloudFormation template<a name="w4aac13c29c17d179c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.