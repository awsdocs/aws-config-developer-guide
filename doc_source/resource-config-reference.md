# Supported Resource Types<a name="resource-config-reference"></a>

AWS Config supports the following AWS resources types and resource relationships\. 
+ Some AWS Regions support a subset of these resource types\. For information on which resource types are supported in which Regions, see [Resource Coverage by Region Availability](https://docs.aws.amazon.com/config/latest/developerguide/what-is-resource-config-coverage.html)\.
+ Advanced queries for AWS Config supports a subset of these resource types\. For a list of those supported resource types, see [Supported Resource Types for Advanced Queries](https://github.com/awslabs/aws-config-resource-schema/tree/master/config/properties/resource-types)\.
+ Proactive evaluation for AWS Config supports a subset of these resource types\. For a list of those supported resource types, see [Supported Resource Types for Proactive Evaluation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html#aws-config-rules-evaluation-modes)\.
+ Periodic rules can run on resources that AWS Config recording does not support and can be run without the configuration recorder being enabled\. Periodic rules do not depend on configuration items\. For more information on the difference between change–triggered rules and periodic rules, see [Evaluation Mode and Trigger Types for AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html)\.

**Note**  
When AWS Config onboards new resource types, the default resources for the new resource types will be discovered during the account baselining process\. If you have the configuration recorder set up to record all supported resource types, you may receive notifications for default resources while a new resource type is in the process of onboarding\. The public documentation is updated once the onboarding process is complete\.

## Amazon AppStream 2\.0<a name="appstream"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon AppStream 2\.0 | AWS::AppStream::DirectoryConfig | NA | NA | 

## Amazon API Gateway<a name="amazonapigateway"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

To learn more about how AWS Config integrates with Amazon API Gateway, see [Monitoring API Gateway API Configuration with AWS Config](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-config.html)\.

## Amazon Athena<a name="amazonathena"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon CloudFront<a name="amazoncloudfront"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon CloudWatch<a name="amazoncloudwatch"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon CloudWatch | AWS::CloudWatch::Alarm | NA | NA | 
| Amazon CloudWatch RUM | AWS::RUM::AppMonitor | NA | NA | 

## Amazon CodeGuru<a name="amazoncodeguru"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon CodeGuru Reviewer | AWS::CodeGuruReviewer::RepositoryAssociation | NA | NA | 

## Amazon Connect<a name="amazonconnect"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon Detective<a name="amazondetective"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon Detective | AWS::Detective::Graph | NA | NA | 

## Amazon DynamoDB<a name="amazondynamodb"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon DynamoDB | AWS::DynamoDB::Table | NA | NA | 

## Amazon Elastic Compute Cloud<a name="amazonelasticcomputecloud"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*AWS Config records the configuration details of Dedicated hosts and the instances that you launch on them\. As a result, you can use AWS Config as a data source when you report compliance with your server\-bound software licenses\. For example, you can view the configuration history of an instance and determine which Amazon Machine Image \(AMI\) it is based on\. Then, you can look up the configuration history of the host, which includes details such as the numbers of sockets and cores, to check that the host complies with the license requirements of the AMI\. For more information, see [Tracking Configuration Changes with AWS Config](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-aws-config.html) in the *Amazon EC2 User Guide for Linux Instances*\. 

\*The EC2 SecurityGroup Properties definition contains IP CIDR blocks, which are converted to IP ranges internally, and may return unexpected results when trying to find a specific IP range\. For workarounds to search for specific IP ranges, see [Limitations for Advanced Queries](https://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html#query-limitations)\.

## Amazon Elastic Container Registry<a name="amazonelasticcontainerregistry"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon Elastic Container Registry Public<a name="amazonelasticcontainerregistrypublic"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon Elastic Container Registry Public | AWS::ECR::PublicRepository | NA | NA | 

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
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon EMR<a name="amazonemr"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon EMR | AWS::EMR::SecurityConfiguration | NA | NA | 

## Amazon EventBridge<a name="amazoneventbridge"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon Fraud Detector<a name="amazonfrauddetector"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon GuardDuty<a name="amazonguardduty"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## HealthLake<a name="healthlake"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| HealthLake | AWS::HealthLake::FHIRDatastore | NA | NA | 

## Amazon Interactive Video Service<a name="amazoninteractivevideoservice"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon OpenSearch Service<a name="amazonopensearchservice"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

**Note**  
On September 8, 2021, Amazon Elasticsearch Service was renamed to Amazon OpenSearch Service\. OpenSearch Service supports OpenSearch as well as legacy Elasticsearch OSS\. For more information, see [Amazon OpenSearch Service \- Summary of changes](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html)\.  
You may continue to see your data for `AWS::OpenSearch::Domain` under the existing `AWS::Elasticsearch::Domain` resource type for several weeks, even if you upgrade one or more domains to OpenSearch\.

## Amazon Pinpoint<a name="amazonpinpoint"></a>


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

## Amazon Lex<a name="amazonlex"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon Lightsail<a name="amazonlightsail"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon Lookout for Metrics<a name="amazonlookoutmetrics"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon Lookout for Metrics | AWS::LookoutMetrics::Alert | NA | NA | 

## Lookout for Vision<a name="amazonlookoutvision"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Lookout for Vision | AWS::LookoutVision::Project | NA | NA | 

## Amazon MQ<a name="amazonmq"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon MQ | AWS::AmazonMQ::Broker | NA | NA | 

## Amazon Managed Streaming for Apache Kafka<a name="amazonmsk"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| Amazon Managed Streaming for Apache Kafka | AWS::MSK::Cluster | NA | NA | 

## Amazon Redshift<a name="amazonredshift"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon Relational Database Service<a name="amazonrelationaldatabaseservice"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon Route 53<a name="amazonroute53"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon SageMaker<a name="amazonsagemaker"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon Simple Email Service<a name="amazonsimpleemailservice"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

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

\*If you configured AWS Config to record your S3 buckets, and are not receiving configuration change notifications, check that your S3 bucket policies have the required permissions\. For more information, see [Managing Permissions for S3 Bucket Recording](iamrole-permissions.md#troubleshooting-recording-s3-bucket-policy)\. 

**Amazon S3 Bucket Attributes**

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

For more information about the attributes, see [Bucket Configuration Options](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#bucket-config-options-intro) in the *Amazon Simple Storage Service User Guide*\.

## Amazon Virtual Private Cloud<a name="amazonvirtualprivatecloud"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## Amazon WorkSpaces<a name="amazonworkspaces"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS AppConfig<a name="awsappconfig"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS AppSync<a name="awsappsync"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS AppSync | AWS::AppSync::GraphQLApi | NA | NA | 

## AWS Auto Scaling<a name="awsautoscaling"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Backup<a name="awsbackup"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

Due to how AWS Backup works, some of these resource types relate to the other AWS Backup resource types in this table\.

`AWS::Backup::BackupPlan` is related to `AWS::Backup::BackupSelection` where a Backup Plan has many selections, and `AWS::Backup::BackupVault` is related to `AWS::Backup::RecoveryPoint` where an AWS Backup Vault has multiple recovery points\.

For more information, see [Managing backups using backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html) and [Working with backup vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html)\.

## AWS Batch<a name="awsbatch"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Budgets<a name="awsbudgets"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS Budgets | AWS::Budgets::BudgetsAction | NA | NA | 

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

## AWS Cloud9<a name="awscloud9"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS Cloud9 | AWS::Cloud9::EnvironmentEC2 | NA | NA | 

## AWS Cloud Map<a name="awscloudmap"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS CodeBuild<a name="awscodebuild"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*To learn more about how AWS Config integrates with AWS CodeBuild, see [Use AWS Config with AWS CodeBuild Sample](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-integrate-config.html)\.

## AWS CodeDeploy<a name="awscodedeploy"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS CodePipeline<a name="awscodepipeline"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*AWS Config records configuration changes to CodePipeline pipelines and supported resource types in the pipelines\. AWS Config does not record configuration changes for resource types in the pipelines that are not yet supported\. Unsupported resource types such as `CodeCommit repository, CodeDeploy application, ECS cluster,` and `ECS service` appear in the supplementary configuration section of the configuration item for the stack\. 

## AWS Config<a name="awsconfig"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*The relationship between `AWS::Config::ResourceCompliance` and a related resource depends on how `AWS::Config::ResourceCompliance` reports compliance for that specific resource type\.

\*`AWS::Config::ConfigurationRecorder` is a system resource type of AWS Config and recording of this resource type is enabled by default\.

**Note**  
Recording for the `AWS::Config::ConformancePackCompliance` and `AWS::Config::ConfigurationRecorder` resource types come with no additional charge\.

## AWS Database Migration Service<a name="awsdms"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS DataSync<a name="awsdatasync"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Device Farm<a name="awsdevicefarm"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS Device Farm | AWS::DeviceFarm::TestGridProject | NA | NA | 

## AWS Elastic Beanstalk<a name="awselasticbeanstalk"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Fault Injection Simulator<a name="awsfis"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS Fault Injection Simulator | AWS::FIS::ExperimentTemplate | NA | NA | 

## AWS Global Accelerator<a name="awsglobalaccelerator"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Glue<a name="awsglue"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Identity and Access Management<a name="awsiam"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

AWS Config includes inline policies with the configuration details that it records\. For more information on inline policies, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#inline-policies) in the IAM User Guide\.

## AWS IoT<a name="awsiot"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Key Management Service<a name="awskeymanagementservice"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Lambda Function<a name="awslambdafunction"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Network Firewall<a name="awsnetworkfirewall"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Resilience Hub<a name="awsresiliencehub"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS Resilience Hub | AWS::ResilienceHub::ResiliencyPolicy | NA | NA | 

## AWS RoboMaker<a name="awsrobomaker"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Secrets Manager<a name="awssecretsmanager"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Service Catalog<a name="servicecatalog"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Shield<a name="awsshield"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Step Functions<a name="awsstepfunctions"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Systems Manager<a name="awssystemsmanager"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

\*To learn more about managed instance inventory, see [Recording Software Configuration for Managed Instances](recording-managed-instance-inventory.md)\.

## AWS Transfer Family<a name="awstransferfamily"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS Transfer Family | AWS::Transfer::Workflow | NA | NA | 

## AWS WAF<a name="awswaf"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS X\-Ray<a name="awsxray"></a>


****  

| AWS Service | Resource Type Value | Relationship | Related Resource | 
| --- | --- | --- | --- | 
| AWS X\-Ray | AWS::XRay::EncryptionConfig | NA | NA | 

## Elastic Load Balancing<a name="elasticloadbalancing"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)

## AWS Elemental MediaPackage<a name="mediapackage"></a>


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)