# iam\-policy\-no\-statements\-with\-admin\-access<a name="iam-policy-no-statements-with-admin-access"></a>

Checks whether the default version of AWS Identity and Access Management \(IAM\) policies do not have administrator access\. If any statement has "Effect": "Allow" with "Action": "\*" over "Resource": "\*", the rule is non\-compliant\. 

**Identifier:** IAM\_POLICY\_NO\_STATEMENTS\_WITH\_ADMIN\_ACCESS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template<a name="w24aac11c29c17b7d211c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.