# elb\-acm\-certificate\-required<a name="elb-acm-certificate-required"></a>

Checks if the Classic Load Balancers use SSL certificates provided by AWS Certificate Manager\. To use this rule, use an SSL or HTTPS listener with your Classic Load Balancer\. This rule is only applicable to Classic Load Balancers\. This rule does not check Application Load Balancers and Network Load Balancers\.

**Identifier:** ELB\_ACM\_CERTIFICATE\_REQUIRED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w29aac11c33c17b7d167c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.