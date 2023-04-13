# s3\-bucket\-default\-lock\-enabled<a name="s3-bucket-default-lock-enabled"></a>

Checks whether Amazon S3 bucket has lock enabled, by default\. The rule is NON\_COMPLIANT if the lock is not enabled\. 

**Identifier:** S3\_BUCKET\_DEFAULT\_LOCK\_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

mode \(Optional\)Type: String  
mode: \(optional\): A mode parameter with valid values of GOVERNANCE or COMPLIANCE\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d521c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.