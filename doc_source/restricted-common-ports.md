# restricted\-common\-ports<a name="restricted-common-ports"></a>

Checks whether the security groups in use do not allow unrestricted incoming TCP traffic to the specified ports\. The rule is COMPLIANT when the IP addresses for inbound TCP connections are restricted to the specified ports\. This rule applies only to IPv4\.  

**Identifier:** RESTRICTED\_INCOMING\_TRAFFIC

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

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

## AWS CloudFormation template<a name="w22aac11c29c17d271c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.