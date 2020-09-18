# ec2\-instance\-managed\-by\-systems\-manager<a name="ec2-instance-managed-by-systems-manager"></a>

Checks whether the Amazon EC2 instances in your account are managed by AWS Systems Manager\.

**Note**  
This rule does not consider changes in the `PingStatus` of an instance in Systems Manager, for example, Status \- Connection Lost\. The rule reports such instances as compliant\.

**Identifier:** EC2\_INSTANCE\_MANAGED\_BY\_SSM

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

None  

## AWS CloudFormation template<a name="w22aac11c29c17d117c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.