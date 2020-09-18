# ec2\-managedinstance\-applications\-required<a name="ec2-managedinstance-applications-required"></a>

Checks whether all of the specified applications are installed on the instance\. Optionally, specify the minimum acceptable version\. You can also specify the platform to apply the rule only to instances running that platform\.

**Note**  
Ensure that SSM agent is running on the EC2 instance and configure SSM agents\. 

**Identifier:** EC2\_MANAGEDINSTANCE\_APPLICATIONS\_REQUIRED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

applicationNames  
Comma\-separated list of application names\. Optionally, specify versions appended with ":" \(for example, "Chrome:0\.5\.3, FireFox"\)\.   
**Note** The application names must be an exact match\. For example, use **firefox** on Linux or **firefox\-compat** on Amazon Linux\. In addition, AWS Config does not currently support wildcards for the *applicationNames* parameter \(for example, **firefox\***\)\.

platformType  
 The platform type \(for example, "Linux" or "Windows"\)\. 

## AWS CloudFormation template<a name="w22aac11c29c17d125c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.