# cloudfront\-security\-policy\-check<a name="cloudfront-security-policy-check"></a>

Checks if Amazon CloudFront distributions are using a minimum security policy and cipher suite of TLSv1\.2 or greater for viewer connections\. This rule is NON\_COMPLIANT for a CloudFront distribution if the minimumProtocolVersion is below TLSv1\.2\_2018\. 

**Identifier:** CLOUDFRONT\_SECURITY\_POLICY\_CHECK

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East \(N\. Virginia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9c89c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.