# elb\-acm\-certificate\-required<a name="elb-acm-certificate-required"></a>

Checks if the Classic Load Balancers use SSL certificates provided by AWS Certificate Manager\. To use this rule, use an SSL or HTTPS listener with your Classic Load Balancer\. This rule is only applicable to Classic Load Balancers\. This rule does not check Application Load Balancers and Network Load Balancers\.

**Identifier:** ELB\_ACM\_CERTIFICATE\_REQUIRED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Asia Pacific \(Osaka\), Europe \(Milan\), AWS GovCloud \(US\-East\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c31c27b9d287c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.