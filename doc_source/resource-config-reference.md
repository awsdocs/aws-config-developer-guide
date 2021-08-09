# Supported Resource Types<a name="resource-config-reference"></a>

AWS Config supports the following AWS resources types and resource relationships\.

Advanced Queries for AWS Config supports a subset of these resource types\. For a list of those supported resource types, see [Support Resource Types for Advanced Queries](https://github.com/awslabs/aws-config-resource-schema/tree/master/config/properties/resource-types)\.

## Amazon API Gateway<a name="amazonapigateway"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

To learn more about how AWS Config integrates with Amazon API Gateway, see [Monitoring API Gateway API Configuration with AWS Config](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-config.html)\.

## Amazon CloudFront<a name="amazoncloudfront"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*AWS Config support for Amazon CloudFront is available only in the US East \(N\. Virginia\) region\.

## Amazon CloudWatch<a name="amazoncloudwatch"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon CloudWatch | AWS::CloudWatch::Alarm | NA | NA | 

## Amazon DynamoDB<a name="amazondynamodb"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon DynamoDB | AWS::DynamoDB::Table | NA | NA | 

## Amazon Elastic Block Store<a name="amazonelasticblockstore"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon Elastic Block Store | AWS::EC2::Volume | is attached to | EC2 instance | 

## Amazon Elastic Compute Cloud<a name="amazonelasticcomputecloud"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*AWS Config records the configuration details of Dedicated hosts and the instances that you launch on them\. As a result, you can use AWS Config as a data source when you report compliance with your server\-bound software licenses\. For example, you can view the configuration history of an instance and determine which Amazon Machine Image \(AMI\) it is based on\. Then, you can look up the configuration history of the host, which includes details such as the numbers of sockets and cores, to verify that the host complies with the license requirements of the AMI\. For more information, see [Tracking Configuration Changes with AWS Config ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-aws-config.html) in the *Amazon EC2 User Guide for Linux Instances*\. 

## Amazon Elastic Container Registry<a name="amazonelasticcontainerregistry"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon Elastic Container Registry | AWS::ECR::Repository | NA | NA | 

## Amazon Elastic Container Service<a name="amazonelasticcontainerservice"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*This service currently only support the new Amazon Resource Name \(ARN\) format\. For more information, see [Amazon Resource Names \(ARNs\) and IDs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids) in the ECS developer guide\.

Old \(not supported\): `arn:aws:ecs:region:aws_account_id:service/service-name`

New \(supported\): `arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name`

## Amazon Elastic File System<a name="amazonelasticfilesystem"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon Elastic Kubernetes Service<a name="amazonelastickubernetesservice"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon Elastic Kubernetes Service | AWS::EKS::Cluster | NA | NA | 

## Amazon Elasticsearch Service<a name="amazonelasticsearchservice"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon Quantum Ledger Database \(Amazon QLDB\)<a name="amazonqldb"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon QLDB | AWS::QLDB::Ledger | NA | NA | 

## Amazon Kinesis<a name="amazonkinesis"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon Redshift<a name="amazonredshift"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon Relational Database Service<a name="amazonrelationaldatabaseservice"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon S3 Bucket Attributes<a name="s3-attributes"></a>

AWS Config also records the following attributes for the Amazon S3 bucket resource type\.


****  

| Attributes | Description | 
| --- | --- | 
| AccelerateConfiguration | Transfer acceleration for data over long distances between your client and a bucket\. | 
| BucketAcl | Access control list used to manage access to buckets and objects\.  | 
| BucketPolicy | Policy that defines the permissions to the bucket\.  | 
| CrossOriginConfiguration | Allow cross\-origin requests to the bucket\.  | 
| LifecycleConfiguration | Rules that define the lifecycle for objects in your bucket\.  | 
| LoggingConfiguration | Logging used to track requests for access to the bucket\.  | 
| NotificationConfiguration | Event notifications used to send alerts or trigger workflows for specified bucket events\.  | 
| ReplicationConfiguration | Automatic, asynchronous copying of objects across buckets in different AWS Regions\.  | 
| RequestPaymentConfiguration | Requester pays is enabled\.  | 
| TaggingConfiguration | Tags added to the bucket to categorize\. You can also use tagging to track billing\.  | 
| WebsiteConfiguration | Static website hosting is enabled for the bucket\. | 
| VersioningConfiguration | Versioning is enabled for objects in the bucket\.  | 

For more information about the attributes, see [Bucket Configuration Options](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#bucket-config-options-intro) in the *Amazon Simple Storage Service Developer Guide*\.

## Amazon Simple Notification Service<a name="amazonsimplenotificationservice"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon Simple Notification Service | AWS::SNS::Topic | NA | NA | 

## Amazon Simple Queue Service<a name="amazonsimplequeueservice"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon Simple Queue Service | AWS::SQS::Queue | NA | NA | 

## Amazon Simple Storage Service<a name="amazonsimplestorageservice"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*If you configured AWS Config to record your S3 buckets, and are not receiving configuration change notifications, verify your S3 bucket policies have the required permissions\. For more information, see [Managing Permissions for S3 Bucket Recording](iamrole-permissions.md#troubleshooting-recording-s3-bucket-policy)\. 

## Amazon Virtual Private Cloud<a name="amazonvirtualprivatecloud"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Auto Scaling<a name="autoscaling"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Backup<a name="awsbackup"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

Due to how AWS Backup works, some of these resource types relate to the other AWS Backup resource types in this table\.

`AWS::Backup::BackupPlan` is related to `AWS::Backup::BackupSelection` where a Backup Plan has many selections, and `AWS::Backup::BackupVault` is related to `AWS::Backup::RecoveryPoint` where an AWS Backup Vault has multiple recovery points\.

For more information, see [Managing backups using backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html) and [Working with backup vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html)\.

## AWS Certificate Manager<a name="awscertificatemanager"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS Certificate Manager | AWS::ACM::Certificate | NA | NA | 

## AWS CloudFormation<a name="awscloudformation"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS CloudFormation | AWS::CloudFormation::Stack\* | contains | Supported AWS resource types | 

\*AWS Config records configuration changes to AWS CloudFormation stacks and supported resource types in the stacks\. AWS Config does not record configuration changes for resource types in the stack that are not yet supported\. Unsupported resource types appear in the supplementary configuration section of the configuration item for the stack\. 

## AWS CloudTrail<a name="awscloudtrail"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS CloudTrail | AWS::CloudTrail::Trail | NA | NA | 

## AWS CodeBuild<a name="awscodebuild"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*To learn more about how AWS Config integrates with AWS CodeBuild, see [Use AWS Config with AWS CodeBuild Sample](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-integrate-config.html)\.

## AWS CodePipeline<a name="awscodepipeline"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*AWS Config records configuration changes to CodePipeline pipelines and supported resource types in the pipelines\. AWS Config does not record configuration changes for resource types in the pipelines that are not yet supported\. Unsupported resource types such as `CodeCommit repository, CodeDeploy application, ECS cluster,` and `ECS service` appear in the supplementary configuration section of the configuration item for the stack\. 

## AWS Config<a name="awsconfig"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*The relationship between `AWS::Config::ResourceCompliance` and a related resource depends on how `AWS::Config::ResourceCompliance` reports compliance for that specific resource type\.

**Note**  
Recording for the `AWS::Config::ConformancePackCompliance` resource type is available at no additional charge\.

## AWS Elastic Beanstalk<a name="awselasticbeanstalk"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Identity and Access Management<a name="awsiam"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*AWS Identity and Access Management \(IAM\) resources are *global resources*\. Global resources are not tied to an individual region and can be used in all regions\. The configuration details for a global resource are the same in all regions\. For more information, see [Selecting Which Resources AWS Config Records](select-resources.md)\.

AWS Config includes inline policies with the configuration details that it records\.

## AWS Key Management Service<a name="awskeymanagementservice"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS Key Management Service | AWS::KMS::Key | NA | NA | 

## AWS Lambda Function<a name="awslambdafunction"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Network Firewall<a name="awsnetworkfirewall"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

AWS Config support for Network Firewall is available only in the US East \(N\. Virginia\), Europe \(Ireland\) and US West \(Oregon\) regions\.

## AWS Secrets Manager<a name="awssecretsmanager"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Service Catalog<a name="servicecatalog"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Shield<a name="awsshield"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*AWS Config support for `AWS::Shield::Protection` is available only in the US East \(N\. Virginia\) region\. The `AWS::ShieldRegional::Protection` is available in all regions where AWS Shield is supported\. 

## AWS Systems Manager<a name="awssystemsmanager"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*To learn more about managed instance inventory, see [Recording Software Configuration for Managed Instances](recording-managed-instance-inventory.md)\.

## AWS WAF<a name="awswaf"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*The AWS WAF resource type values are available only in the US East \(N\. Virginia\) Region\. The `AWS::WAFRegional::RateBasedRule`, `AWS::WAFRegional::Rule`, `AWS::WAFRegional::WebACL`, and `AWS::WAFRegional::RuleGroup` are available in all regions where AWS WAF is supported\. 


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*The AWS WAFv2 resource type values are available in all the AWS Regions where AWS WAFv2 is supported\. 

## AWS X\-Ray<a name="awsxray"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS X\-Ray | AWS::XRay::EncryptionConfig | NA | NA | 

## Elastic Load Balancing<a name="elasticloadbalancing"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)