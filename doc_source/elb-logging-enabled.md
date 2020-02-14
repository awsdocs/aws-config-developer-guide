# elb\-logging\-enabled<a name="elb-logging-enabled"></a>

Checks whether the Application Load Balancers and the Classic Load Balancers have logging enabled\. The rule is NON\_COMPLIANT if the `access_logs.s3.enabled` is false or `access_logs.S3.bucket` is not equal to the s3BucketName that you provided\.

**Identifier:** ELB\_LOGGING\_ENABLED

**Trigger type:** Configuration changes

**Parameters:**

 s3BucketNames \(optional\)   
Comma\-separated list of Amazon S3 bucket names for Elastic Load Balancing to deliver the log files\.

## AWS CloudFormation template<a name="w4aac13c29c17d145c13"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.