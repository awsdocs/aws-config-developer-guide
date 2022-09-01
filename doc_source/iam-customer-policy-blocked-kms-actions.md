# iam\-customer\-policy\-blocked\-kms\-actions<a name="iam-customer-policy-blocked-kms-actions"></a>

Checks if the managed AWS Identity and Access Management \(IAM\) policies that you create do not allow blocked actions on AWS KMS keys\. The rule is NON\_COMPLIANT if any blocked action is allowed on AWS KMS keys by the managed IAM policy\. 

**Note**  
This rule does not evalute the conditions provided in IAM policies\. For more information on IAM conditions, see [IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the IAM User Guide\.

**Identifier:** IAM\_CUSTOMER\_POLICY\_BLOCKED\_KMS\_ACTIONS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

blockedActionsPatternsType: CSV  
Comma\-separated list of blocked KMS action patterns, for example, kms:\*, kms:Decrypt, kms:ReEncrypt\*\.

excludePermissionBoundaryPolicy \(Optional\)Type: boolean  
Boolean flag to exclude the evaluation of IAM policies used as permissions boundaries\. If set to 'true', the rule will not include permissions boundaries in the evaluation\. Otherwise, all IAM policies in scope are evaluated when value is set to 'false\.' Default value is 'false'\.

## AWS CloudFormation template<a name="w85aac12c32c17b9d321c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.