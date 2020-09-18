# alb\-waf\-enabled<a name="alb-waf-enabled"></a>

Checks if Web Application Firewall \(WAF\) is enabled on Application Load Balancers \(ALBs\)\. This rule is NON\_COMPLIANT if `key: waf.enabled` is set to false\. 

**Identifier:** ALB\_WAF\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Milan\), Africa \(Cape Town\) Regions

**Parameters:**

wafWebAclIds \(Optional\)Type: CSV  
Comma separated list of web ACL ID \(for WAF\) or web ACL ARN \(for WAFV2\) checking for ALB association\.

## AWS CloudFormation template<a name="w22aac11c29c17c23c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.