# vpc\-default\-security\-group\-closed<a name="vpc-default-security-group-closed"></a>

Checks if the default security group of any Amazon Virtual Private Cloud \(VPC\) does not allow inbound or outbound traffic\. The rule returns NOT\_APPLICABLE if the security group is not default\. The rule is NON\_COMPLIANT if the default security group has one or more inbound or outbound traffic rules\.

**Identifier:** VPC\_DEFAULT\_SECURITY\_GROUP\_CLOSED

**Resource Types:** AWS::EC2::SecurityGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d571c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.