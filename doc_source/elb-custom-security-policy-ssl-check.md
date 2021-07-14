# elb\-custom\-security\-policy\-ssl\-check<a name="elb-custom-security-policy-ssl-check"></a>

Checks whether your Classic Load Balancer SSL listeners are using a custom policy\. The rule is only applicable if there are SSL listeners for the Classic Load Balancer\. 

**Identifier:** ELB\_CUSTOM\_SECURITY\_POLICY\_SSL\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS GovCloud \(US\-East\), Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

sslProtocolsAndCiphersType: String  
Comma\-separated list of ciphers and protocols\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d179c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.