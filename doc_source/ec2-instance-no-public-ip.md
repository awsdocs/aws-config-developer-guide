# ec2\-instance\-no\-public\-ip<a name="ec2-instance-no-public-ip"></a>

Checks whether Amazon Elastic Compute Cloud \(Amazon EC2\) instances have a public IP association\. The rule is NON\_COMPLIANT if the `publicIp` field is present in the Amazon EC2 instance configuration item\. This rule applies only to IPv4\.

**Identifier:** EC2\_INSTANCE\_NO\_PUBLIC\_IP

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

None  

## AWS CloudFormation template<a name="w22aac11c29c17d119c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.