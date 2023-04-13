# cloudtrail\-s3\-dataevents\-enabled<a name="cloudtrail-s3-dataevents-enabled"></a>

Checks whether at least one AWS CloudTrail trail is logging Amazon S3 data events for all S3 buckets\. The rule is NON\_COMPLIANT if trails log data events for S3 buckets is not configured\. 

**Identifier:** CLOUDTRAIL\_S3\_DATAEVENTS\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

S3BucketNames \(Optional\)Type: String  
Comma\-separated list of S3 bucket names for which data events logging should be enabled\. Default behavior checks for all S3 buckets\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d107c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.