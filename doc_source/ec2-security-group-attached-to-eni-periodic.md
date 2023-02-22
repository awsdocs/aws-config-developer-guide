# ec2\-security\-group\-attached\-to\-eni\-periodic<a name="ec2-security-group-attached-to-eni-periodic"></a>

Checks if non\-default security groups are attached to Elastic network interfaces \(ENIs\)\. The rule is NON\_COMPLIANT if the security group is not associated with an ENI\. Security groups not owned by the calling account evaluate as NOT\_APPLICABLE\. 

**Identifier:** EC2\_SECURITY\_GROUP\_ATTACHED\_TO\_ENI\_PERIODIC

**Resource Types:** AWS::EC2::SecurityGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d219c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.