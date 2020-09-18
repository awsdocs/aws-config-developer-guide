# ec2\-managedinstance\-applications\-blacklisted<a name="ec2-managedinstance-applications-blacklisted"></a>

Checks that none of the specified applications are installed on the instance\. Optionally, specify the application version\. Newer versions of the application will not be blacklisted\. You can also specify the platform to apply the rule only to instances running that platform\.

**Identifier:** EC2\_MANAGEDINSTANCE\_APPLICATIONS\_BLACKLISTED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

applicationNames  
Comma\-separated list of application names\. Optionally, specify versions appended with ":" \(for example, "Chrome:0\.5\.3, FireFox"\)\.  
**Note** The application names must be an exact match\. For example, use **firefox** on Linux or **firefox\-compat** on Amazon Linux\. In addition, AWS Config does not currently support wildcards for the *applicationNames* parameter \(for example, **firefox\***\)\.

platformType  
 The platform type \(for example, "Linux" or "Windows"\)\. 

## AWS CloudFormation template<a name="w22aac11c29c17d123c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.