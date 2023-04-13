# s3\-bucket\-acl\-prohibited<a name="s3-bucket-acl-prohibited"></a>

Checks if Amazon Simple Storage Service \(Amazon S3\) Buckets allow user permissions through access control lists \(ACLs\)\. The rule is NON\_COMPLIANT if ACLs are configured for user access in Amazon S3 Buckets\. 

**Identifier:** S3\_BUCKET\_ACL\_PROHIBITED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), China \(Ningxia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d517c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.