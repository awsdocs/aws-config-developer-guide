# cloudfront\-sni\-enabled<a name="cloudfront-sni-enabled"></a>

Checks if Amazon CloudFront distributions are using a custom SSL certificate and are configured to use SNI to serve HTTPS requests\. This rule is NON\_COMPLIANT if a custom SSL certificate is associated but the SSL support method is a dedicated IP address\. 

**Identifier:** CLOUDFRONT\_SNI\_ENABLED

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East \(N\. Virginia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9c91c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.