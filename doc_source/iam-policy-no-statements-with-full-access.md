# iam\-policy\-no\-statements\-with\-full\-access<a name="iam-policy-no-statements-with-full-access"></a>

Checks if AWS Identity and Access Management \(IAM\) policies grant permissions to all actions on individual AWS resources\. The rule is NON\_COMPLIANT if the managed IAM policy allows full access to at least 1 AWS service\. 

**Note**  
This rule only evaluates managed policies\. This rule does NOT evaluate inline policies\. For more information on the difference, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) in the IAM User Guide\.

**Identifier:** IAM\_POLICY\_NO\_STATEMENTS\_WITH\_FULL\_ACCESS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

excludePermissionBoundaryPolicy \(Optional\)Type: boolean  
Boolean flag to ignore evaluation of IAM policies if used only as a permission boundary\. The IAM policy is evaluated when value is False\. Default is False\.

## AWS CloudFormation template<a name="w76aac11c31c17b7d303c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.