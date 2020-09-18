# iam\-policy\-blacklisted\-check<a name="iam-policy-blacklisted-check"></a>

Checks whether for each IAM resource, a policy ARN in the input parameter is attached to the IAM resource\. The rule is NON\_COMPLIANT if the policy ARN is attached to the IAM resource\. AWS Config marks the resource as COMPLIANT if the IAM resource is part of the `exceptionList` parameter irrespective of the presence of the policy ARN\.

**Identifier:** IAM\_POLICY\_BLACKLISTED\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

 policyArns  
Comma\-separated list of policy ARNs\. 

 exceptionList  
Comma\-separated list IAM users, groups, or roles that are exempt from this rule\. For example, users:\[user1;user2\], groups:\[group1;group2\], roles:\[role1;role2;role3\]\.

## AWS CloudFormation template<a name="w22aac11c29c17d201c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.