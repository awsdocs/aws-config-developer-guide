# iam\-policy\-no\-statements\-with\-full\-access<a name="iam-policy-no-statements-with-full-access"></a>

Checks if AWS Identity and Access Management \(IAM\) policies that you create grant permissions to all actions on individual AWS resources\. The rule is NON\_COMPLIANT if any customer managed IAM policy allows full access to at least 1 AWS service\. 

**Note**  
This rule only evaluates customer managed policies\. This rule does NOT evaluate inline policies or AWS managed policies\. For more information on the difference, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) in the IAM User Guide\.

**Identifier:** IAM\_POLICY\_NO\_STATEMENTS\_WITH\_FULL\_ACCESS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

excludePermissionBoundaryPolicy \(Optional\)Type: boolean  
Boolean flag to exclude the evaluation of IAM policies used as permissions boundaries\. If set to 'true', the rule will not include permissions boundaries in the evaluation\. Otherwise, all IAM policies in scope are evaluated when value is set to 'false\.' Default value is 'false'\.

## AWS CloudFormation template<a name="w2aac12c31c27b9d337c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.