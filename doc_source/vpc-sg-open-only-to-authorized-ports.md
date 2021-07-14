# vpc\-sg\-open\-only\-to\-authorized\-ports<a name="vpc-sg-open-only-to-authorized-ports"></a>

Checks whether any security groups with inbound 0\.0\.0\.0/0 have TCP or UDP ports accessible\. The rule is NON\_COMPLIANT when a security group with inbound 0\.0\.0\.0/0 has a port accessible which is not specified in the rule parameters\. 

**Identifier:** VPC\_SG\_OPEN\_ONLY\_TO\_AUTHORIZED\_PORTS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\) Region

**Parameters:**

authorizedTcpPorts \(Optional\)Type: String  
 Comma\-separated list of TCP ports authorized to be open to 0\.0\.0\.0/0\. Ranges are defined by dash, for example, "443,1020\-1025"\.

authorizedUdpPorts \(Optional\)Type: String  
 Comma\-separated list of UDP ports authorized to be open to 0\.0\.0\.0/0\. Ranges are defined by dash, for example, "500,1020\-1025"\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d375c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.