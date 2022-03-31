# ec2\-managedinstance\-inventory\-blacklisted<a name="ec2-managedinstance-inventory-blacklisted"></a>

Checks whether instances managed by Amazon EC2 Systems Manager are configured to collect blacklisted inventory types\. 

**Identifier:** EC2\_MANAGEDINSTANCE\_INVENTORY\_BLACKLISTED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\) Region

**Parameters:**

inventoryNamesType: CSV  
Comma separated list of Systems Manager inventory types \(for example, 'AWS:Network, AWS:WindowsUpdate'\)\.

platformType \(Optional\)Type: String  
Platform type \(for example, 'Linux'\)\.

## AWS CloudFormation template<a name="w76aac11c31c17b7d175c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.