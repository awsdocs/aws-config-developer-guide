# vpc\-vpn\-2\-tunnels\-up<a name="vpc-vpn-2-tunnels-up"></a>

Checks that both VPN tunnels provided by AWS Site\-to\-Site VPN are in UP status\. The rule returns NON\_COMPLIANT if one or both tunnels are in DOWN status\. 

**Identifier:** VPC\_VPN\_2\_TUNNELS\_UP

**Resource Types:** AWS::EC2::VPNConnection

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(Bahrain\), China \(Beijing\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), China \(Ningxia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d613c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.