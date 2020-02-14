# vpc\-sg\-open\-only\-to\-authorized\-ports<a name="vpc-sg-open-only-to-authorized-ports"></a>

Checks whether the security group with 0\.0\.0\.0/0 of any Amazon Virtual Private Cloud \(Amazon VPC\) allows only specific inbound TCP or UDP traffic\. The rule and any security group with inbound 0\.0\.0\.0/0\. are NON\_COMPLIANT if you do not provide any ports in the parameters\.

**Identifier:** VPC\_SG\_OPEN\_ONLY\_TO\_AUTHORIZED\_PORTS

**Trigger type:** Configuration changes

**Parameters:**

authorizedTcpPorts \(Optional\)  
Comma\-separated list of TCP ports authorized to be open to 0\.0\.0\.0/0\. Ranges are defined by a dash; for example, "443,1020\-1025"\.

authorizedUdpPorts \(Optional\)  
Comma\-separated list of UDP ports authorized to be open to 0\.0\.0\.0/0\. Ranges are defined by a dash; for example, "500,1020\-1025"\.

## AWS CloudFormation template<a name="w4aac13c29c17d275c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.