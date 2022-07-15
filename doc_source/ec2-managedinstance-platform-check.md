# ec2\-managedinstance\-platform\-check<a name="ec2-managedinstance-platform-check"></a>

Checks whether EC2 managed instances have the desired configurations\. 

**Identifier:** EC2\_MANAGEDINSTANCE\_PLATFORM\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\) Region

**Parameters:**

platformTypeType: String  
Platform type \(for example, 'Linux'\)\.

platformVersion \(Optional\)Type: String  
Platform version \(for example, '2016\.09'\)\.

agentVersion \(Optional\)Type: String  
Agent version \(for example, '2\.0\.433\.0'\)\.

platformName \(Optional\)Type: String  
The version of the platform \(for example, '2016\.09'\)

## AWS CloudFormation template<a name="w79aac11c32c17b9d201c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.