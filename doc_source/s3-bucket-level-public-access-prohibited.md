# s3\-bucket\-level\-public\-access\-prohibited<a name="s3-bucket-level-public-access-prohibited"></a>

Checks if Amazon Simple Storage Service \(Amazon S3\) buckets are publicly accessible\. This rule is NON\_COMPLIANT if an Amazon S3 bucket is not listed in the `excludedPublicBuckets` parameter and bucket level settings are public\. 

**Identifier:** S3\_BUCKET\_LEVEL\_PUBLIC\_ACCESS\_PROHIBITED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

excludedPublicBuckets \(Optional\)Type: CSV  
Comma\-separated list of known allowed public Amazon S3 bucket names\.

## AWS CloudFormation template<a name="w2aac12c31c27b9d483c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.