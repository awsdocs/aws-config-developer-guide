# cloudfront\-associated\-with\-waf<a name="cloudfront-associated-with-waf"></a>

Checks if Amazon CloudFront distributions are associated with either AWS WAF or WAFv2 web access control lists \(ACLs\)\. This rule is COMPLIANT if the CloudFront distribution is associated with a web ACL\. This rule is NON\_COMPLIANT if a CloudFront distribution is not associated with a web ACL\. 

**Identifier:** CLOUDFRONT\_ASSOCIATED\_WITH\_WAF

**Trigger type:** Configuration changes

**AWS Region:** Only available in the US East \(N\. Virginia\) Region

**Parameters:**

wafWebAclIds \(Optional\)Type: CSV  
Comma\-separated list of web ACL IDs for AWS WAF or web ACL Amazon Resource Names \(ARNs\) for WAFV2\.

## AWS CloudFormation template<a name="w24aac11c29c17c45c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.