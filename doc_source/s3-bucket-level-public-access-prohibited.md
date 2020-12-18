# s3\-bucket\-level\-public\-access\-prohibited<a name="s3-bucket-level-public-access-prohibited"></a>

Checks if Amazon Simple Storage Service \(Amazon S3\) buckets are publicly accessible\. The rule is COMPLIANT if all public Amazon S3 buckets are listed in the `excludedPublicBuckets` parameter\. The rule is NON\_COMPLIANT if an Amazon S3 bucket is not listed in the `excludedPublicBuckets` parameter and bucket level settings are public\. 

**Identifier:** S3\_BUCKET\_LEVEL\_PUBLIC\_ACCESS\_PROHIBITED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), and AWS GovCloud \(US\-West\)

**Parameters:**

excludedPublicBuckets \(Optional\)Type: CSV  
Comma\-separated list of known allowed public Amazon S3 bucket names\.

## AWS CloudFormation template<a name="w24aac11c29c17d305c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.