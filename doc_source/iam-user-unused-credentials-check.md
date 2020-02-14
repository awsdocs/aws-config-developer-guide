# iam\-user\-unused\-credentials\-check<a name="iam-user-unused-credentials-check"></a>

Checks whether your AWS Identity and Access Management \(IAM\) users have passwords or active access keys that have not been used within the specified number of days you provided\. Re\-evaluating this rule within 4 hours of the first evaluation will have no effect on the results\.

**Identifier:** IAM\_USER\_UNUSED\_CREDENTIALS\_CHECK

**Trigger type:** Periodic

**Parameters:**

 maxCredentialUsageAge  
Maximum number of days within which a credential must be used\. The default value is 90 days\.

## AWS CloudFormation template<a name="w4aac13c29c17d191c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.