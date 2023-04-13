# ec2\-managedinstance\-patch\-compliance\-status\-check<a name="ec2-managedinstance-patch-compliance-status-check"></a>

Checks whether the compliance status of the AWS Systems Manager patch compliance is COMPLIANT or NON\_COMPLIANT after the patch installation on the instance\. The rule is compliant if the field status is COMPLIANT\. 

**Identifier:** EC2\_MANAGEDINSTANCE\_PATCH\_COMPLIANCE\_STATUS\_CHECK

**Resource Types:** AWS::SSM::PatchCompliance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(Bahrain\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d217c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.