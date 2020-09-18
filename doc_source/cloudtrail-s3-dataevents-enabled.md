# cloudtrail\-s3\-dataevents\-enabled<a name="cloudtrail-s3-dataevents-enabled"></a>

Checks whether at least one AWS CloudTrail trail is logging Amazon S3 data events for all S3 buckets\. The rule is NON\_COMPLIANT if trails that log data events for S3 buckets are not configured\.

**Note**  
The rule checks for trails in their home region only\. The rule does not evaluate shadow or organization trails\. The rule does not support Amazon S3 prefixes\.

**Identifier:** CLOUDTRAIL\_S3\_DATAEVENTS\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions

**Parameters:**

 S3BucketNames  
\(Optional\) Comma\-separated list of S3 bucket names for which data events logging should be enabled\. Default behavior checks for all S3 buckets\.

## AWS CloudFormation template<a name="w22aac11c29c17c59c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.