# iam\-user\-group\-membership\-check<a name="iam-user-group-membership-check"></a>

Checks whether IAM users are members of at least one IAM group\. 

**Identifier:** IAM\_USER\_GROUP\_MEMBERSHIP\_CHECK

**Resource Types:** AWS::IAM::User

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

groupNames \(Optional\)Type: String  
Comma\-separated list of IAM groups in which IAM users must be members\.  
This rule does not support group names with commas\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d379c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.