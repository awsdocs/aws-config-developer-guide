# cloudfront\-traffic\-to\-origin\-encrypted<a name="cloudfront-traffic-to-origin-encrypted"></a>

Checks if Amazon CloudFront distributions are encrypting traffic to custom origins\. The rule is NON\_COMPLIANT if ‘OriginProtocolPolicy’ is ‘http\-only’ or if ‘OriginProtocolPolicy’ is ‘match\-viewer’ and ‘ViewerProtocolPolicy’ is ‘allow\-all’\. 

**Identifier:** CLOUDFRONT\_TRAFFIC\_TO\_ORIGIN\_ENCRYPTED

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East \(N\. Virginia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w85aac12c32c17b9c87c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.