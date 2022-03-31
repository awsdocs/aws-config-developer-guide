# iam\-user\-unused\-credentials\-check<a name="iam-user-unused-credentials-check"></a>

Checks if your AWS Identity and Access Management \(IAM\) users have passwords or active access keys that have not been used within the specified number of days you provided\. The rule is NON\_COMPLIANT if there are inactive accounts not recently used\.

**Note**  
Re\-evaluating this rule within 4 hours of the first evaluation will have no effect on the results\.

**Identifier:** IAM\_USER\_UNUSED\_CREDENTIALS\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

maxCredentialUsageAgeType: intDefault: 90  
Maximum number of days a credential cannot be used\. The default value is 90 days\.

## AWS CloudFormation template<a name="w76aac11c31c17b7d315c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.