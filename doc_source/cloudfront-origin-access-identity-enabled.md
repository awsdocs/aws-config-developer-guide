# cloudfront\-origin\-access\-identity\-enabled<a name="cloudfront-origin-access-identity-enabled"></a>

Checks if Amazon CloudFront distribution with S3 Origin type has Origin Access Identity \(OAI\) configured\. The rule is NON\_COMPLIANT if the CloudFront distribution is backed by S3 and any of S3 Origin type is not OAI configured or if the origin is not an S3 bucket\.

**Note**  
The rule does not return NOT\_APPLICABLE if the origin is not an S3 bucket\.

**Identifier:** CLOUDFRONT\_ORIGIN\_ACCESS\_IDENTITY\_ENABLED

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East \(N\. Virginia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9c93c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.