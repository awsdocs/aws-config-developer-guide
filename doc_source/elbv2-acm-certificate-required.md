# elbv2\-acm\-certificate\-required<a name="elbv2-acm-certificate-required"></a>

Checks if Application Load Balancers and Network Load Balancers have listeners that are configured to use certificates from AWS Certificate Manager \(ACM\)\. This rule is NON\_COMPLIANT if at least 1 load balancer has at least 1 listener that is configured without a certificate from ACM or is configured with a certificate different from an ACM certificate\.

**Identifier:** ELBV2\_ACM\_CERTIFICATE\_REQUIRED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

AcmCertificatesAllowed \(Optional\)Type: CSV  
Comma\-separated list of certificate Amazon Resource Names \(ARNs\)\.

## AWS CloudFormation template<a name="w2aac12c31c27b9d283c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.