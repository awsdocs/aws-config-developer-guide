# ec2\-security\-group\-attached\-to\-eni<a name="ec2-security-group-attached-to-eni"></a>

Checks if non\-default security groups are attached to Elastic network interfaces \(ENIs\)\. The rule is NON\_COMPLIANT if the security group is not associated with an elastic network interface \(ENI\)\. 

**Important**  
This rule is being deprecated due to [Indirect Relationship Deprecation](https://docs.aws.amazon.com/config/latest/developerguide/faq.html#faq) as configuration items triggering this rule will not longer be created once indirect relationships are deprecated\. If you use this rule, please remove it from evaluating the configuration of AWS resources and replace it with the new [ec2\-security\-group\-attached\-to\-eni\-periodic](https://docs.aws.amazon.com/config/latest/developerguide/ec2-security-group-attached-to-eni-periodic.html) rule\. The [ec2\-security\-group\-attached\-to\-eni\-periodic](https://docs.aws.amazon.com/config/latest/developerguide/ec2-security-group-attached-to-eni-periodic.html) rule will not be impacted by this deprecation as it is triggered on a periodic basis rather than on configuration changes\.

**Identifier:** EC2\_SECURITY\_GROUP\_ATTACHED\_TO\_ENI

**Resource Types:** AWS::EC2::SecurityGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d217c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.