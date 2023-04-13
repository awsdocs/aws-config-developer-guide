# restricted\-common\-ports<a name="restricted-common-ports"></a>

Checks if the security groups in use do not allow unrestricted incoming TCP traffic to the specified ports\. The rule is COMPLIANT when the IP addresses for inbound TCP connections are restricted to the specified ports\. This rule applies only to IPv4\. 

**Identifier:** RESTRICTED\_INCOMING\_TRAFFIC

**Resource Types:** AWS::EC2::SecurityGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

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

## AWS CloudFormation template<a name="w2aac12c33c15b9d507c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.