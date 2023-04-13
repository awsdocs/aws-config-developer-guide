# iam\-policy\-in\-use<a name="iam-policy-in-use"></a>

Checks whether the IAM policy ARN is attached to an IAM user, or a group with one or more IAM users, or an IAM role with one or more trusted entity\. 

**Identifier:** IAM\_POLICY\_IN\_USE

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

policyARNType: String  
An IAM policy ARN to be checked\.

policyUsageType \(Optional\)Type: String  
Specify whether you expect the policy to be attached to an IAM user, group or role\. Valid values are IAM\_USER, IAM\_GROUP, IAM\_ROLE, or ANY\. Default value is ANY\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d369c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.