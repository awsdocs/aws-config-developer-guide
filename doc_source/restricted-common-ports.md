# restricted\-common\-ports<a name="restricted-common-ports"></a>

Checks whether the incoming SSH traffic for the security groups is accessible to the specified ports\. The rule is COMPLIANT when the IP addresses of the incoming SSH traffic in the security group are restricted to the specified ports\. This rule applies only to IPv4\. 

**Identifier:** RESTRICTED\_INCOMING\_TRAFFIC

**Trigger type:** Configuration changes

**Parameters:**

 blockedPort1   
 Blocked TCP port number\. 

 blockedPort2   
 Blocked TCP port number\. 

 blockedPort3   
 Blocked TCP port number\. 

 blockedPort4   
 Blocked TCP port number\. 

 blockedPort5   
 Blocked TCP port number\. 

## AWS CloudFormation template<a name="w4aac13c29c17d229c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.