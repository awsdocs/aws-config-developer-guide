# restricted\-common\-ports<a name="restricted-common-ports"></a>

Checks if the security groups in use do not allow unrestricted incoming TCP traffic to the specified ports\. The rule is COMPLIANT when the IP addresses for inbound TCP connections are restricted to the specified ports\. This rule applies only to IPv4\. 

**Identifier:** RESTRICTED\_INCOMING\_TRAFFIC

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

blockedPort1 \(Optional\)Type: intDefault: 20  
Blocked TCP port number\.

blockedPort2 \(Optional\)Type: intDefault: 21  
Blocked TCP port number\.

blockedPort3 \(Optional\)Type: intDefault: 3389  
Blocked TCP port number\.

blockedPort4 \(Optional\)Type: intDefault: 3306  
Blocked TCP port number\.

blockedPort5 \(Optional\)Type: intDefault: 4333  
Blocked TCP port number\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d303c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.