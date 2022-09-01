# alb\-waf\-enabled<a name="alb-waf-enabled"></a>

Checks if Web Application Firewall \(WAF\) is enabled on Application Load Balancers \(ALBs\)\. This rule is NON\_COMPLIANT if key: waf\.enabled is set to false\. 

**Identifier:** ALB\_WAF\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

wafWebAclIds \(Optional\)Type: CSV  
Comma separated list of web ACL ID \(for WAF\) or web ACL ARN \(for WAFV2\) checking for ALB association\.

## AWS CloudFormation template<a name="w85aac12c32c17b9c13c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.