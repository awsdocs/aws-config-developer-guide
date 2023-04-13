# iam\-role\-managed\-policy\-check<a name="iam-role-managed-policy-check"></a>

Checks if all AWS managed policies specified in the list of managed policies are attached to the AWS Identity and Access Management \(IAM\) role\. The rule is NON\_COMPLIANT if an AWS managed policy is not attached to the IAM role\. 

**Identifier:** IAM\_ROLE\_MANAGED\_POLICY\_CHECK

**Resource Types:** AWS::IAM::Role

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

managedPolicyArnsType: CSV  
Comma\-separated list of AWS managed policy Amazon Resource Names \(ARNs\)\. For more information, see [Amazon Resource Names \(ARNs\)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) and [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) in the *IAM User Guide*\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d375c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.