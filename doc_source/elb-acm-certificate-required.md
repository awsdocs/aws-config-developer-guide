# elb\-acm\-certificate\-required<a name="elb-acm-certificate-required"></a>

Checks if the Classic Load Balancers use SSL certificates provided by AWS Certificate Manager\. To use this rule, use an SSL or HTTPS listener with your Classic Load Balancer\. This rule is only applicable to Classic Load Balancers\. This rule does not check Application Load Balancers and Network Load Balancers\.

**Identifier:** ELB\_ACM\_CERTIFICATE\_REQUIRED

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), AWS GovCloud \(US\-East\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d297c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.