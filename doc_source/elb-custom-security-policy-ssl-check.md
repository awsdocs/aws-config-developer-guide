# elb\-custom\-security\-policy\-ssl\-check<a name="elb-custom-security-policy-ssl-check"></a>

Checks whether your Classic Load Balancer SSL listeners are using a custom policy\. The rule is only applicable if there are SSL listeners for the Classic Load Balancer\. 

**Identifier:** ELB\_CUSTOM\_SECURITY\_POLICY\_SSL\_CHECK

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), AWS GovCloud \(US\-East\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

sslProtocolsAndCiphersType: String  
Comma separated list of ciphers and protocols\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d301c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.