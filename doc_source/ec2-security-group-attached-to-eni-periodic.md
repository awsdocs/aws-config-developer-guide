# ec2\-security\-group\-attached\-to\-eni\-periodic<a name="ec2-security-group-attached-to-eni-periodic"></a>

Checks if non\-default security groups are attached to Elastic network interfaces \(ENIs\)\. The rule is NON\_COMPLIANT if the security group is not associated with an elastic network interface \(ENI\)\. 

**Identifier:** EC2\_SECURITY\_GROUP\_ATTACHED\_TO\_ENI\_PERIODIC

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w79aac11c32c17b7d211c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.