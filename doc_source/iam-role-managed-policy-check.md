# iam\-role\-managed\-policy\-check<a name="iam-role-managed-policy-check"></a>

Checks that AWS Identity and Access Management \(IAM\) policies in a list of policies are attached to all AWS roles\. The rule is NON\_COMPLIANT if the IAM managed policy is not attached to the IAM role\.

**Identifier:** IAM\_ROLE\_MANAGED\_POLICY\_CHECK

**Trigger type:** Configuration changes

**Parameters:**

 managedPolicyNames  
Comma\-separated list of AWS managed policy ARNs\.

## AWS CloudFormation template<a name="w4aac13c29c17d181c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.