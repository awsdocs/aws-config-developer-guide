# vpc\-default\-security\-group\-closed<a name="vpc-default-security-group-closed"></a>

Checks that the default security group of any Amazon Virtual Private Cloud \(VPC\) does not allow inbound or outbound traffic\. The rule returns NOT\_APPLICABLE if the security group is not default\. The rule is NON\_COMPLIANT if the default security group has one or more inbound or outbound traffic\.

**Identifier:** VPC\_DEFAULT\_SECURITY\_GROUP\_CLOSED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

 None  

## AWS CloudFormation template<a name="w22aac11c29c17d325c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.