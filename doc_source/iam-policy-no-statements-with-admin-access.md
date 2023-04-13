# iam\-policy\-no\-statements\-with\-admin\-access<a name="iam-policy-no-statements-with-admin-access"></a>

Checks if AWS Identity and Access Management \(IAM\) policies that you create have Allow statements that grant permissions to all actions on all resources\. The rule is NON\_COMPLIANT if any customer managed IAM policy statement includes "Effect": "Allow" with "Action": "\*" over "Resource": "\*"\.

**Note**  
This rule only evaluates customer managed policies\. This rule does NOT evaluate inline policies or AWS managed policies\. For more information on the difference, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) in the IAM User Guide\.

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

**Identifier:** IAM\_POLICY\_NO\_STATEMENTS\_WITH\_ADMIN\_ACCESS

**Resource Types:** AWS::IAM::Policy

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

excludePermissionBoundaryPolicy \(Optional\)Type: boolean  
Boolean flag to exclude the evaluation of IAM policies used as permissions boundaries\. If set to 'true', the rule will not include permissions boundaries in the evaluation\. Otherwise, all IAM policies in scope are evaluated when value is set to 'false\.' Default value is 'false'\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d371c27"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.