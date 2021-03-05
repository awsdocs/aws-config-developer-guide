# elb\-acm\-certificate\-required<a name="elb-acm-certificate-required"></a>

This rule checks whether the Elastic Load Balancer\(s\) uses SSL certificates provided by AWS Certificate Manager\. You must use an SSL or HTTPS listener with your Elastic Load Balancer to use this rule\. 

**Identifier:** ELB\_ACM\_CERTIFICATE\_REQUIRED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w24aac11c29c17b7d161c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.