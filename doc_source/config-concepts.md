# Concepts<a name="config-concepts"></a>

AWS Config provides a detailed view of the resources associated with your AWS account, including how they are configured, how they are related to one another, and how the configurations and their relationships have changed over time\. Let's take a closer look at the concepts of AWS Config\.

**Contents**
+ [AWS Config](#config-platform-concept)
  + [AWS Resources](#aws-resources)
  + [Configuration History](#config-history)
  + [Configuration Items](#config-items)
  + [Configuration Recorder](#config-recorder)
  + [Configuration Snapshot](#config-snapshot)
  + [Configuration Stream](#config-stream)
  + [Resource Relationship](#resource-relationship)
+ [AWS Config Managed and Custom Rules](#aws-config-rules)
  + [AWS Config Custom Rules](#aws-config-custom-rules)
+ [Multi\-Account Multi\-Region Data Aggregation](#multi-account-multi-region-data-aggregation)
  + [Source Account](#source-accounts)
  + [Source Region](#source-region)
  + [Aggregator](#aggregator)
  + [Aggregator Account](#aggregator-accounts)
  + [Authorization](#authorization)
+ [Managing AWS Config](#config-concepts-manage)
  + [AWS Config Console](#config-concepts-console)
  + [AWS Config CLI](#config-concepts-cli)
  + [AWS Config APIs](#config-concepts-api)
  + [AWS SDKs](#config-concepts-sdk)
+ [Control Access to AWS Config](#config-concepts-iam)
+ [Partner Solutions](#config-concepts-partner-solutions)

## AWS Config<a name="config-platform-concept"></a>

Understanding the basic components of AWS Config will help you track resource inventory and changes and evaluate configurations of your AWS resources\. 

### AWS Resources<a name="aws-resources"></a>

*AWS resources* are entities that you create and manage using the AWS Management Console, the AWS Command Line Interface \(CLI\), the AWS SDKs, or AWS partner tools\. Examples of AWS resources include Amazon EC2 instances, security groups, Amazon VPCs, and Amazon Elastic Block Store\. AWS Config refers to each resource using its unique identifier, such as the resource ID or an [Amazon Resource Name \(ARN\)](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#ARN)\. For details, see [Supported Resource Types](resource-config-reference.md)\.

### Configuration History<a name="config-history"></a>

A configuration history is a collection of the configuration items for a given resource over any time period\. A configuration history can help you answer questions about, for example, when the resource was first created, how the resource has been configured over the last month, and what configuration changes were introduced yesterday at 9 AM\. The configuration history is available to you in multiple formats\. AWS Config automatically delivers a configuration history file for each resource type that is being recorded to an Amazon S3 bucket that you specify\. You can select a given resource in the AWS Config console and navigate to all previous configuration items for that resource using the timeline\. Additionally, you can access the historical configuration items for a resource from the API\.

### Configuration Items<a name="config-items"></a>

A *configuration item* represents a point\-in\-time view of the various attributes of a supported AWS resource that exists in your account\. The components of a configuration item include metadata, attributes, relationships, current configuration, and related events\. AWS Config creates a configuration item whenever it detects a change to a resource type that it is recording\. For example, if AWS Config is recording Amazon S3 buckets, AWS Config creates a configuration item whenever a bucket is created, updated, or deleted\.

For more information, see [Components of a Configuration Item](config-item-table.md)\.

### Configuration Recorder<a name="config-recorder"></a>

The configuration recorder stores the configurations of the supported resources in your account as configuration items\. You must first create and then start the configuration recorder before you can start recording\. You can stop and restart the configuration recorder at any time\. For more information, see [Managing the Configuration Recorder](stop-start-recorder.md)\.

By default, the configuration recorder records all supported resources in the region where AWS Config is running\. You can create a customized configuration recorder that records only the resource types that you specify\. For more information, see [Selecting Which Resources AWS Config Records](select-resources.md)\.

If you use the AWS Management Console or the CLI to turn on the service, AWS Config automatically creates and starts a configuration recorder for you\.

### Configuration Snapshot<a name="config-snapshot"></a>

A configuration snapshot is a collection of the configuration items for the supported resources that exist in your account\. This configuration snapshot is a complete picture of the resources that are being recorded and their configurations\. The configuration snapshot can be a useful tool for validating your configuration\. For example, you may want to examine the configuration snapshot regularly for resources that are configured incorrectly or that potentially should not exist\. The configuration snapshot is available in multiple formats\. You can have the configuration snapshot delivered to an Amazon Simple Storage Service \(Amazon S3\) bucket that you specify\. Additionally, you can select a point in time in the AWS Config console and navigate through the snapshot of configuration items using the relationships between the resources\.

### Configuration Stream<a name="config-stream"></a>

A configuration stream is an automatically updated list of all configuration items for the resources that AWS Config is recording\. Every time a resource is created, modified, or deleted, AWS Config creates a configuration item and adds to the configuration stream\. The configuration stream works by using an Amazon Simple Notification Service \(Amazon SNS\) topic of your choice\. The configuration stream is helpful for observing configuration changes as they occur so that you can spot potential problems, generating notifications if certain resources are changed, or updating external systems that need to reflect the configuration of your AWS resources\. 

### Resource Relationship<a name="resource-relationship"></a>

AWS Config discovers AWS resources in your account and then creates a map of relationships between AWS resources\. For example, a relationship might include an Amazon EBS volume `vol-123ab45d` attached to an Amazon EC2 instance `i-a1b2c3d4` that is associated with security group `sg-ef678hk`\. 

For more information, see [Supported Resource Types](resource-config-reference.md)\.

## AWS Config Managed and Custom Rules<a name="aws-config-rules"></a>

An AWS Config rule represents your desired configuration settings for specific AWS resources or for an entire AWS account\. AWS Config provides customizable, predefined rules to help you get started\. If a resource violates a rule, AWS Config flags the resource and the rule as noncompliant, and AWS Config notifies you through Amazon SNS\.

### AWS Config Custom Rules<a name="aws-config-custom-rules"></a>

With AWS Config you can also create custom rules\. While AWS Config continuously tracks your resource configuration changes, it checks whether these changes violate any of the conditions in your rules\.

After you activate a rule, AWS Config compares your resources to the conditions of the rule\. After this initial evaluation, AWS Config continues to run evaluations each time one is triggered\. The evaluation triggers are defined as part of the rule, and they can include the following types:
+ Configuration changes – AWS Config triggers the evaluation when any resource that matches the rule's scope changes in configuration\. The evaluation runs after AWS Config sends a configuration item change notification\.
+ Periodic – AWS Config runs evaluations for the rule at a frequency that you choose \(for example, every 24 hours\)\.

For more information, see [Evaluating Resources with AWS Config Rules](evaluate-config.md)\.

## Multi\-Account Multi\-Region Data Aggregation<a name="multi-account-multi-region-data-aggregation"></a>

Multi\-account multi\-region data aggregation in AWS Config allows you to aggregate AWS Config configuration and compliance data from multiple accounts and regions into a single account\. Multi\-account multi\-region data aggregation is useful for central IT administrators to monitor compliance for multiple AWS accounts in the enterprise\.

### Source Account<a name="source-accounts"></a>

A source account is the AWS account from which you want to aggregate AWS Config resource configuration and compliance data\. A source account can be an individual account or an organization in AWS Organizations\. You can provide source accounts individually or you can retrieve them through AWS Organizations\.

### Source Region<a name="source-region"></a>

A source region is the AWS region from which you want to aggregate AWS Config configuration and compliance data\.

### Aggregator<a name="aggregator"></a>

An aggregator is a new resource type in AWS Config that collects AWS Config configuration and compliance data from multiple source accounts and regions\. Create an aggregator in the region where you want to see the aggregated AWS Config configuration and compliance data\. 

### Aggregator Account<a name="aggregator-accounts"></a>

An aggregator account is an account where you create an aggregator\.

### Authorization<a name="authorization"></a>

As a source account owner, authorization refers to the permissions you grant to an aggregator account and region to collect your AWS Config configuration and compliance data\. Authorization is not required if you are aggregating source accounts that are part of AWS Organizations\.

For more information, see topics in [Multi\-Account Multi\-Region Data Aggregation](aggregate-data.md) section\.

## Managing AWS Config<a name="config-concepts-manage"></a>

### AWS Config Console<a name="config-concepts-console"></a>

You can manage the service using the AWS Config console\. The console provides a user interface for performing many AWS Config tasks such as:
+ Specifying the types of AWS resources for recording\.
+ Configuring resources to record, including:
  + Selecting an Amazon S3 bucket\.
  + Selecting an Amazon SNS topic\.
  + Creating AWS Config role\.
+ Creating managed rules and custom rules that represent desired configuration settings for specific AWS resources or for an entire AWS account\.
+ Creating and managing configuration aggregators to aggregate data across multiple accounts and regions\.
+ Viewing a snapshot of current configurations of the supported resources\.
+ Viewing relationships between AWS resources\.

For more information about the AWS Management Console, see [AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/getting-started.html)\. 

### AWS Config CLI<a name="config-concepts-cli"></a>

The AWS Command Line Interface is a unified tool that you can use to interact with AWS Config from the command line\. For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/)\. For a complete list of AWS Config CLI commands, see [Available Commands](https://docs.aws.amazon.com/cli/latest/reference/configservice/index.html)\.

### AWS Config APIs<a name="config-concepts-api"></a>

In addition to the console and the CLI, you can also use the AWS Config RESTful APIs to program AWS Config directly\. For more information, see the [AWS Config API Reference](https://docs.aws.amazon.com/config/latest/APIReference/)\.

### AWS SDKs<a name="config-concepts-sdk"></a>

As an alternative to using the AWS Config API, you can use one of the AWS SDKs\. Each SDK consists of libraries and sample code for various programming languages and platforms\. The SDKs provide a convenient way to create programmatic access to AWS Config\. For example, you can use the SDKs to sign requests cryptographically, manage errors, and retry requests automatically\. For more information, see the [Tools for Amazon Web Services](https://aws.amazon.com/tools/) page\.

## Control Access to AWS Config<a name="config-concepts-iam"></a>

AWS Identity and Access Management is a web service that enables Amazon Web Services \(AWS\) customers to manage users and user permissions\. Use IAM to create individual users for anyone who needs access to AWS Config\. Create an IAM user for yourself, give that IAM user administrative privileges, and use that IAM user for all of your work\. By creating individual IAM users for people accessing your account, you can give each IAM user a unique set of security credentials\. You can also grant different permissions to each IAM user\. If necessary, you can change or revoke an IAM user’s permissions at any time\. For more information, see [AWS Identity and Access Management](security-iam.md)\.

## Partner Solutions<a name="config-concepts-partner-solutions"></a>

AWS partners with third\-party specialists in logging and analysis to provide solutions that use AWS Config output\. For more information, visit the AWS Config detail page at [ AWS Config](https://aws.amazon.com/config)\.