# Setting Up AWS Config with the AWS CLI<a name="gs-cli"></a>

You can use the AWS Command Line Interface to control and automate the services from AWS\. For more information about the AWS CLI and for instructions on installing the AWS CLI tools, see the following in the *AWS Command Line Interface User Guide*\.
+ [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/)
+ [Getting Set Up with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html) 

## Features<a name="gs-cli-features.title"></a>

You can use the AWS Command Line Interface to get started with AWS Config to do the following:

**Resource management**
+ Specify the resource types you want AWS Config to record\.
+ Set up an Amazon S3 bucket to receive a configuration snapshot on request and configuration history\.
+ Set up Amazon SNS to send configuration stream notifications\.
+ Grant AWS Config the permissions it needs to access the Amazon S3 bucket and the Amazon SNS topic\.

  For more information, see [Viewing AWS Resource Configurations and History](https://docs.aws.amazon.com/config/latest/developerguide/view-manage-resource.html) and [Managing AWS Resource Configurations and History](https://docs.aws.amazon.com/config/latest/developerguide/manage-config.html)\.

**Rules and conformance packs**
+ Specify the rules that you want AWS Config to use to evaluate compliance information for the recorded resource types\.
+ Use conformance packs, or a collection of AWS Config rules and remediation actions that can be deployed and monitored as a single entity in your AWS account\.

  For more information, see [Evaluating Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) and [Conformance Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html)\.

**Aggregators**
+ Use an aggregator to get a centralized view of your resource inventory and compliance\. An aggregator is an AWS Config resource type that collects AWS Config configuration and compliance data from multiple AWS accounts and AWS Regions into a single account and Region\.

  For more information, see [Multi\-Account Multi\-Region Data Aggregation ](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html)\.

**Advanced queries**
+ Use one of the sample queries or write your own query by referring to the configuration schema of the AWS resource\.

  For more information, see [Querying the Current Configuration State of AWS Resources ](https://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html)\. 

## Setting up<a name="gs-cli-setting-up.title"></a>

See the following topics to set up AWS Config with the AWS CLI\.

**Topics**
+ [Features](#gs-cli-features.title)
+ [Setting up](#gs-cli-setting-up.title)
+ [Prerequisites](gs-cli-prereq.md)
+ [Turning on AWS Config](gs-cli-subscribe.md)
+ [Check that AWS Config Is On](gs-cli-verify-subscribe.md)