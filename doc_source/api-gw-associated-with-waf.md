# api\-gw\-associated\-with\-waf<a name="api-gw-associated-with-waf"></a>

Checks if an Amazon API Gateway API stage is using an AWS WAF Web ACL\. This rule is NON\_COMPLIANT if an AWS WAF Web ACL is not used or if a used AWS Web ACL does not match what is listed in the rule parameter\. 

**Identifier:** API\_GW\_ASSOCIATED\_WITH\_WAF

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

WebAclArns \(Optional\)Type: CSV  
Comma\-separated list of web ACL Amazon Resource Names \(ARNs\)\.

## AWS CloudFormation template<a name="w2aac12c31c27b9c15c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.