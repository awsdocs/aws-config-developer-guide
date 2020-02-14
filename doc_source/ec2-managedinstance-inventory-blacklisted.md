# ec2\-managedinstance\-inventory\-blacklisted<a name="ec2-managedinstance-inventory-blacklisted"></a>

Checks whether instances managed by AWS Systems Manager are configured to collect blacklisted inventory types\.

**Identifier:** EC2\_MANAGEDINSTANCE\_INVENTORY\_BLACKLISTED

**Trigger type:** Configuration changes

**Parameters:**

 inventoryNames   
Comma\-separated list of Systems Manager inventory types \(for example, "AWS:Network, AWS:WindowsUpdate"\)\.

 platformType   
Platform type \(for example, “Linux”\)\.

## AWS CloudFormation template<a name="w4aac13c29c17d119c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.