# elb\-logging\-enabled<a name="elb-logging-enabled"></a>

Checks whether the Application Load Balancer and the Classic Load Balancer have logging enabled\. The rule is NON\_COMPLIANT if the `access_logs.s3.enabled` is false or `access_logs.S3.bucket` is not equal to the s3BucketName that you provided\.

**Identifier:** ELB\_LOGGING\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

 s3BucketNames \(optional\)   
Comma\-separated list of Amazon S3 bucket names for Elastic Load Balancing to deliver the log files\.

## AWS CloudFormation template<a name="w22aac11c29c17d169c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.