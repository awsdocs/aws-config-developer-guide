# s3\-bucket\-public\-read\-prohibited<a name="s3-bucket-public-read-prohibited"></a>

Checks that your Amazon S3 buckets do not allow public read access\. The rule checks the Block Public Access settings, the bucket policy, and the bucket access control list \(ACL\)\.

 The rule is compliant when both of the following are true:
+ The Block Public Access setting restricts public policies or the bucket policy does not allow public read access\.
+ The Block Public Access setting restricts public ACLs or the bucket ACL does not allow public read access\.

The rule is noncompliant when:
+ If the Block Public Access setting does not restrict public policies, AWS Config evaluates whether the policy allows public read access\. If the policy allows public read access, the rule is noncompliant\.
+ If the Block Public Access setting does not restrict public bucket ACLs, AWS Config evaluates whether the bucket ACL allows public read access\. If the bucket ACL allows public read access, the rule is noncompliant\.

**Identifier:** S3\_BUCKET\_PUBLIC\_READ\_PROHIBITED

**Trigger type:** Configuration changes and Periodic

**AWS Region:** All supported AWS Regions

**Parameters:**

None  

## AWS CloudFormation template<a name="w22aac11c29c17d297c23"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.