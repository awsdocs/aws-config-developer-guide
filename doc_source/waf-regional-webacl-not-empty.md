# waf\-regional\-webacl\-not\-empty<a name="waf-regional-webacl-not-empty"></a>

Checks if a WAF regional Web ACL contains any WAF rules or rule groups\. The rule is NON\_COMPLIANT if there are no WAF rules or rule groups present within a Web ACL\. 

**Identifier:** WAF\_REGIONAL\_WEBACL\_NOT\_EMPTY

**Resource Types:** AWS::WAFRegional::WebACL

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d601c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.