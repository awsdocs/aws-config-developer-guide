# iam\-no\-inline\-policy\-check<a name="iam-no-inline-policy-check"></a>

Checks that inline policy feature is not in use\. The rule is NON\_COMPLIANT if an AWS Identity and Access Management \(IAM\) user, IAM role or IAM group has any inline policy\. 

**Identifier:** IAM\_NO\_INLINE\_POLICY\_CHECK

**Resource Types:** AWS::IAM::User, AWS::IAM::Role, AWS::IAM::Group

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d363c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.