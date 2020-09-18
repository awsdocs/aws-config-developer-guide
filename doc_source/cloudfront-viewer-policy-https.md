# cloudfront\-viewer\-policy\-https<a name="cloudfront-viewer-policy-https"></a>

Checks whether your Amazon CloudFront distributions use HTTPS \(directly or via a redirection\)\. The rule is NON\_COMPLIANT if the value of `ViewerProtocolPolicy` is set to allow\-all for `defaultCacheBehavior` or for `cacheBehaviors`\. This means that the rule is non compliant when viewers can use HTTP or HTTPS\.

**Identifier:** CLOUDFRONT\_VIEWER\_POLICY\_HTTPS

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East \(N\. Virginia\) Region

**Parameters:**

 None  

## AWS CloudFormation template<a name="w22aac11c29c17c49c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.