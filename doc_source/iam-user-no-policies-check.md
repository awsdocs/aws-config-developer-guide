# iam\-user\-no\-policies\-check<a name="iam-user-no-policies-check"></a>

Checks if none of your IAM users have policies attached\. IAM users must inherit permissions from IAM groups or roles\. The rule is NON\_COMPLIANT if there is at least one IAM user with policies attached\.

**Identifier:** IAM\_USER\_NO\_POLICIES\_CHECK

**Resource Types:** AWS::IAM::User

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d357c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.