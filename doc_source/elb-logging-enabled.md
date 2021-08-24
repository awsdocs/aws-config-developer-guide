# elb\-logging\-enabled<a name="elb-logging-enabled"></a>

Checks if the Application Load Balancer and the Classic Load Balancer have logging enabled\. The rule is NON\_COMPLIANT if the `access_logs.s3.enabled` is false or `access_logs.S3.bucket` is not equal to the s3BucketName that you provided\.

**Identifier:** ELB\_LOGGING\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

s3BucketNames \(Optional\)Type: CSV  
Comma\-separated list of Amazon S3 bucket names for Amazon ELB to deliver the log files\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d201c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.