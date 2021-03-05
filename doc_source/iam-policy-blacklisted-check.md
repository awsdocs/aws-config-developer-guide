# iam\-policy\-blacklisted\-check<a name="iam-policy-blacklisted-check"></a>

Checks that none of your IAM users, groups, or roles \(excluding `exceptionList`\) have the specified policies attached\. 

**Identifier:** IAM\_POLICY\_BLACKLISTED\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

policyArnsType: CSVDefault: arn:aws:iam::aws:policy/AdministratorAccess  
Comma separated list of IAM policy arns which should not be attached to any IAM entity\.

exceptionList \(Optional\)Type: CSV  
Comma separated list of resourcetypes and list of resource name pairs\. \(for example, users:\[user1;user2\], groups:\[group1;group2\], roles:\[role1;role2;role3\]\)\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d207c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.