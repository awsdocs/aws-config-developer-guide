# ec2\-security\-group\-attached\-to\-eni<a name="ec2-security-group-attached-to-eni"></a>

Checks that security groups are attached to Amazon Elastic Compute Cloud \(Amazon EC2\) instances or to an elastic network interface\. The rule returns NON\_COMPLIANT if the security group is not associated with an Amazon EC2 instance or an elastic network interface\.

**Identifier:** EC2\_SECURITY\_GROUP\_ATTACHED\_TO\_ENI

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

None  

## AWS CloudFormation template<a name="w22aac11c29c17d135c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.