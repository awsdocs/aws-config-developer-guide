# ec2\-managedinstance\-applications\-required<a name="ec2-managedinstance-applications-required"></a>

Checks whether all of the specified applications are installed on the instance\. Optionally, specify the minimum acceptable version\. Optionally, specify the platform to apply the rule only to instances running that platform\. 

**Identifier:** EC2\_MANAGEDINSTANCE\_APPLICATIONS\_REQUIRED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

applicationNamesType: CSV  
Comma\-separated list of application names\. Optionally, specify versions appended with ':' \(for example, 'Chrome:0\.5\.3, Firefox'\)\.

platformType \(Optional\)Type: String  
Platform type \(for example, 'Linux'\)\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d123c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.