# cloudfront\-origin\-access\-identity\-enabled<a name="cloudfront-origin-access-identity-enabled"></a>

Checks that Amazon CloudFront distribution with Amazon S3 Origin type has Origin Access Identity \(OAI\) configured\. This rule is NON\_COMPLIANT if the CloudFront distribution is backed by Amazon S3 and any of Amazon S3 Origin type is not OAI configured\. 

**Identifier:** CLOUDFRONT\_ORIGIN\_ACCESS\_IDENTITY\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East \(N\. Virginia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w22aac11c29c17c43c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.