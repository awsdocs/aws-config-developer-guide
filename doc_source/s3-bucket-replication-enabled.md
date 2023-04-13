# s3\-bucket\-replication\-enabled<a name="s3-bucket-replication-enabled"></a>

Checks if your Amazon S3 buckets have replication rules enabled\. The rule is NON\_COMPLIANT if an S3 bucket does not have a replication rule or has a replication rule that is not enabled\. 

**Identifier:** S3\_BUCKET\_REPLICATION\_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

ReplicationType \(Optional\)Type: String  
Accepted values: 'CROSS\-REGION' and 'SAME\-REGION'\. Enter 'CROSS\-REGION' for the rule to check that all buckets have only Cross\-Region Replication enabled\. Enter 'SAME\-REGION' for the rule to check that all buckets have only Same\-Region Replication enabled\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d535c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.