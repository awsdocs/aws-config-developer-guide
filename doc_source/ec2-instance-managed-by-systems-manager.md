# ec2\-instance\-managed\-by\-systems\-manager<a name="ec2-instance-managed-by-systems-manager"></a>

Checks whether the Amazon EC2 instances in your account are managed by AWS Systems Manager\.

**Note**  
This rule does not consider changes in the `PingStatus` of an instance in Systems Manager, for example, Status \- Connection Lost\. The rule reports such instances as compliant\.

**Identifier:** EC2\_INSTANCE\_MANAGED\_BY\_SSM

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template<a name="w29aac11c33c17b7d137c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.