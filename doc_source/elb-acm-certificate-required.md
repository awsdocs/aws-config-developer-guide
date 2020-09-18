# elb\-acm\-certificate\-required<a name="elb-acm-certificate-required"></a>

Checks whether the Classic Load Balancers use SSL certificates provided by AWS Certificate Manager\. To use this rule, use an SSL or HTTPS listener with your Classic Load Balancer\. This rule is only applicable to Classic Load Balancers\. This rule does not check Application Load Balancers and Network Load Balancers\.

**Identifier:** ELB\_ACM\_CERTIFICATE\_REQUIRED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 None   

## AWS CloudFormation template<a name="w22aac11c29c17d163c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.