# ec2\-security\-group\-attached\-to\-eni<a name="ec2-security-group-attached-to-eni"></a>

Checks that non\-default security groups are attached to Amazon Elastic Compute Cloud \(EC2\) instances or an elastic network interfaces \(ENIs\)\. The rule returns NON\_COMPLIANT if the security group is not associated with an EC2 instance or an ENI\. 

**Identifier:** EC2\_SECURITY\_GROUP\_ATTACHED\_TO\_ENI

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w29aac11c33c17b7d159c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.