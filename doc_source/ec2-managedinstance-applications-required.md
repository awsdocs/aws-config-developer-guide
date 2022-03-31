# ec2\-managedinstance\-applications\-required<a name="ec2-managedinstance-applications-required"></a>

Checks if all of the specified applications are installed on the instance\. Optionally, specify the minimum acceptable version\. You can also specify the platform to apply the rule only to instances running that platform\.

**Note**  
Ensure that SSM agent is running on the EC2 instance and an association to gather application software inventory is created\. The rule returns NOT\_APPLICABLE if SSM agent is not installed or an association is yet not created or running\.

**Identifier:** EC2\_MANAGEDINSTANCE\_APPLICATIONS\_REQUIRED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\) Region

**Parameters:**

applicationNamesType: CSV  
Comma\-separated list of application names\. Optionally, specify versions appended with ':' \(for example, 'Chrome:0\.5\.3, Firefox'\)\.  
The application names must be an exact match\. For example, use **firefox** on Linux or **firefox\-compat** on Amazon Linux\. In addition, AWS Config does not currently support wildcards for the *applicationNames* parameter \(for example, **firefox\***\)\.

platformType \(Optional\)Type: String  
Platform type \(for example, 'Linux' or 'Windows'\)\.

## AWS CloudFormation template<a name="w76aac11c31c17b7d171c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.