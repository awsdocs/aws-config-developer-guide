# elb\-tls\-https\-listeners\-only<a name="elb-tls-https-listeners-only"></a>

Checks whether your Classic Load Balancer is configured with SSL or HTTPS listeners\. The rule is applicable if a Classic Load Balancer has listeners\. If your Classic Load Balancer does not have a listener configured, then the rule returns NOT\_APPLICABLE\. The rule is COMPLIANT if the Classic Load Balancer listeners is configured with SSL or HTTPS\. The rule is NON\_COMPLIANT if the listener is not configured with SSL or HTTPS\. 

**Identifier:** ELB\_TLS\_HTTPS\_LISTENERS\_ONLY

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

None  

## AWS CloudFormation template<a name="w22aac11c29c17d161c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.