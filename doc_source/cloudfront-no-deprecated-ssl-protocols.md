# cloudfront\-no\-deprecated\-ssl\-protocols<a name="cloudfront-no-deprecated-ssl-protocols"></a>

Checks if CloudFront distributions are using deprecated SSL protocols for HTTPS communication between CloudFront edge locations and custom origins\. This rule is NON\_COMPLIANT for a CloudFront distribution if any ‘OriginSslProtocols’ includes ‘SSLv3’\. 

**Identifier:** CLOUDFRONT\_NO\_DEPRECATED\_SSL\_PROTOCOLS

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East \(N\. Virginia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w79aac11c32c17b7c79c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.