# iam\-policy\-in\-use<a name="iam-policy-in-use"></a>

Checks whether the IAM policy ARN is attached to an IAM user, or an IAM group with one or more IAM users, or an IAM role with one or more trusted entity\.

**Identifier:** IAM\_POLICY\_IN\_USE

**Trigger type:** Periodic

**Parameters:**

 policyArn \(mandatory\)  
An IAM policy Amazon Resource Name \(ARN\) to be checked

 policyUsageType \(optional\)  
Specify the policy to be attached as an IAM user, IAM group, or IAM role\. Valid values are `IAM_USER`, `IAM_GROUP`, `IAM_ROLE`, or `ANY`\. Default value is ANY\.

## AWS CloudFormation template<a name="w4aac13c29c17d177c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.