# cloudfront\-accesslogs\-enabled<a name="cloudfront-accesslogs-enabled"></a>

Checks if Amazon CloudFront distributions are configured to capture information from Amazon Simple Storage Service \(Amazon S3\) server access logs\. This rule is NON\_COMPLIANT if a CloudFront distribution does not have logging configured\. 

**Identifier:** CLOUDFRONT\_ACCESSLOGS\_ENABLED

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East \(N\. Virginia\) Region

**Parameters:**

S3BucketName \(Optional\)Type: String  
The name of the Amazon S3 bucket for storing server access logs\.

## AWS CloudFormation template<a name="w2aac12c33c15b9c83c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.