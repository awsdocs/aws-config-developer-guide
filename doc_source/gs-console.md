# Setting Up AWS Config with the Console<a name="gs-console"></a>

The AWS Management Console provides a quick and streamlined process for setting up AWS Config\.

## Features<a name="gs-console-features.title"></a>

You can use the AWS Management Console to get started with AWS Config to do the following:

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

## Setting up<a name="gs-console-setting-up.title"></a>

**To set up AWS Config with the console**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. If this is the first time you are opening the AWS Config console or you are setting up AWS Config in a new region, the AWS Config console page looks like the following:   
![\[The AWS Config getting started page provides an overview of the service.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/welcome.png)

1. Choose **1\-click setup** to launch AWS Config based on AWS best practices\. You can also choose **Get started** to go through a more detailed setup process\.

**Topics**
+ [Features](#gs-console-features.title)
+ [Setting up](#gs-console-setting-up.title)
+ [1\-click setup](1-click-setup.md)
+ [Manual setup](manual-setup.title.md)