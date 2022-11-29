# alb\-waf\-enabled<a name="alb-waf-enabled"></a>

Checks if Web Application Firewall \(WAF\) is enabled on Application Load Balancers \(ALBs\)\. This rule is NON\_COMPLIANT if key: waf\.enabled is set to false\. 

**Identifier:** ALB\_WAF\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Osaka\), Europe \(Milan\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

wafWebAclIds \(Optional\)Type: CSV  
Comma separated list of web ACL ID \(for WAF\) or web ACL ARN \(for WAFV2\) checking for ALB association\.

## AWS CloudFormation template<a name="w2aac12c31c27b9c13c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.