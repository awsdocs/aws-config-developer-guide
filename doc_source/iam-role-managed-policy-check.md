# iam\-role\-managed\-policy\-check<a name="iam-role-managed-policy-check"></a>

Checks that the AWS Identity and Access Management \(IAM\) role is attached to all AWS managed policies specified in the list of managed policies\. The rule is non\-compliant if the IAM role is not attached to the AWS managed policy\. 

**Identifier:** IAM\_ROLE\_MANAGED\_POLICY\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

managedPolicyArnsType: CSV  
Comma\-separated list of AWS managed policy ARNs\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d219c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.