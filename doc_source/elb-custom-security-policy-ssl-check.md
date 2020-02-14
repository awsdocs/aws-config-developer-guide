# elb\-custom\-security\-policy\-ssl\-check<a name="elb-custom-security-policy-ssl-check"></a>

Checks whether your Classic Load Balancer SSL listeners are using a custom policy\. The rule is only applicable if there are SSL listeners for the Classic Load Balancer\. 

**Identifier:** ELB\_CUSTOM\_SECURITY\_POLICY\_SSL\_CHECK

**Trigger type:** Configuration changes

**Parameters:**

ssl\-protocols\-and\-ciphers  
Comma\-separated list of ciphers and protocol\.

## AWS CloudFormation template<a name="w4aac13c29c17d141c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.