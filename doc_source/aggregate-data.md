# Multi\-Account Multi\-Region Data Aggregation<a name="aggregate-data"></a>

An aggregator is an AWS Config resource type that collects AWS Config configuration and compliance data from the following:
+ Multiple accounts and multiple regions\.
+ Single account and multiple regions\.
+ An organization in AWS Organizations and all the accounts in that organization\.

Use an aggregator to view the resource configuration and compliance data recorded in AWS Config\.

![\[An aggregator collects AWS Config data from multiple accounts and regions.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/Aggregate_Data_Landing_Page_Diagram.png)

For more information about concepts, see [Multi\-Account Multi\-Region Data Aggregation](config-concepts.md#multi-account-multi-region-data-aggregation) section in the Concepts topic\.

To collect your AWS Config data from source accounts and regions, start with:

1. Adding an aggregator to aggregate AWS Config configuration and compliance data from multiple accounts and regions\.

1. Authorizing aggregator accounts to collect AWS Config configuration and compliance data\. Authorization is required when your source accounts are individual accounts\. Authorization is not required if you are aggregating source accounts that are part of AWS Organizations\.

1. Monitoring compliance data for rules and accounts in the aggregated view\.

## Region Support<a name="aggregation-regions"></a>

Currently, multi\-account multi\-region data aggregation is supported in the following regions:


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html)

## Learn More<a name="learn-more-aggregator-landing-page"></a>
+ [Concepts](config-concepts.md)
+ [Viewing Configuration and Compliance Data in the Aggregated View](viewing-the-aggregate-dashboard.md)
+ [Setting Up an Aggregator Using the Console](setup-aggregator-console.md)
+ [Setting Up an Aggregator Using the AWS Command Line Interface](set-up-aggregator-cli.md)
+ [Authorizing Aggregator Accounts to Collect AWS Config Configuration and Compliance Data Using the Console](authorize-aggregator-account-console.md)
+ [Authorizing Aggregator Accounts to Collect AWS Config Configuration and Compliance Data Using the AWS Command Line Interface](authorize-aggregator-account-cli.md)
+ [Troubleshooting for Multi\-Account Multi\-Region Data Aggregation](aggregate-data-troubleshooting.md)