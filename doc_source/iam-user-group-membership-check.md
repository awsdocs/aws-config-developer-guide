# iam\-user\-group\-membership\-check<a name="iam-user-group-membership-check"></a>

Checks whether IAM users are members of at least one IAM group\. 

**Identifier:** IAM\_USER\_GROUP\_MEMBERSHIP\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

groupNames \(Optional\)Type: String  
Comma\-separated list of IAM groups in which IAM users must be members\.  
This rule does not support group names with commas\.

## AWS CloudFormation template<a name="w76aac11c31c17b7d309c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.