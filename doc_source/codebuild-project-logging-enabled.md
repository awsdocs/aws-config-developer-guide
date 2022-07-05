# codebuild\-project\-logging\-enabled<a name="codebuild-project-logging-enabled"></a>

Checks if an AWS CodeBuild project environment has at least one log option enabled\. The rule is NON\_COMPLIANT if 'logsConfig' is not present or the status of all present log configurations is set to 'DISABLED'\. 

**Identifier:** CODEBUILD\_PROJECT\_LOGGING\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

s3BucketNames \(Optional\)Type: String  
Comma\-separated list of Amazon S3 bucket names that logs should be sent to if S3 logs are configured\.

cloudWatchGroupNames \(Optional\)Type: String  
Comma\-separated list of Amazon CloudWatch log group names that logs should be be sent to if CloudWatch logs are configured\.

## AWS CloudFormation template<a name="w79aac11c32c17b7d121c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.