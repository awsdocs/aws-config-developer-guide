# cloudfront\-associated\-with\-waf<a name="cloudfront-associated-with-waf"></a>

Checks if Amazon CloudFront distributions are associated with either WAF or WAFv2 web access control lists \(ACLs\)\. This rule is NON\_COMPLIANT if a CloudFront distribution is not associated with a web ACL\. 

**Identifier:** CLOUDFRONT\_ASSOCIATED\_WITH\_WAF

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East \(N\. Virginia\) Region

**Parameters:**

wafWebAclIds \(Optional\)Type: CSV  
Comma\-separated list of web ACL IDs for WAF or web ACL Amazon Resource Names \(ARNs\) for WAFV2\.

## AWS CloudFormation template<a name="w79aac11c32c17b7c73c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.