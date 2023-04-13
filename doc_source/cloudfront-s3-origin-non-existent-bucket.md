# cloudfront\-s3\-origin\-non\-existent\-bucket<a name="cloudfront-s3-origin-non-existent-bucket"></a>

Checks if Amazon CloudFront distributions point to a non\-existent S3 bucket\. The rule is NON\_COMPLIANT if `S3OriginConfig` for a CloudFront distribution points to a non\-existent S3 bucket\. The rule does not evaluate S3 buckets with static website hosting\. 

**Identifier:** CLOUDFRONT\_S3\_ORIGIN\_NON\_EXISTENT\_BUCKET

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Periodic

**AWS Region:** Only available in US East \(N\. Virginia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9c97c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.