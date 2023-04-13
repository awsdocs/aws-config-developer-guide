# ec2\-paravirtual\-instance\-check<a name="ec2-paravirtual-instance-check"></a>

Checks if the virtualization type of an EC2 instance is paravirtual\. This rule is NON\_COMPLIANT for an EC2 instance if 'virtualizationType' is set to 'paravirtual'\. 

**Identifier:** EC2\_PARAVIRTUAL\_INSTANCE\_CHECK

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe \(Ireland\), Europe \(Frankfurt\), South America \(Sao Paulo\), US East \(N\. Virginia\), Asia Pacific \(Tokyo\), US West \(Oregon\), US West \(N\. California\), Asia Pacific \(Singapore\), Asia Pacific \(Sydney\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d223c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.