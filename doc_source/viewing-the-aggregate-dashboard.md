# Viewing Configuration and Compliance Data in the Aggregator Dashboard<a name="viewing-the-aggregate-dashboard"></a>

The dashboard on the **Aggregators** page displays the configuration data of AWS resources and provides an overview of your rules and their compliance state\. 

It provides the total resource count of AWS resources\. The resource types and source accounts are ranked by the highest number of resources\. It also provides a count of compliant and noncompliant rules\. The noncompliant rules are ranked by highest number of noncompliant resources and source accounts with highest number of noncompliant rules\. 

After setup, AWS Config starts aggregating data from the specified source accounts into an aggregator\. It might take a few minutes for AWS Config to display the compliance status of rules on this page\.

## Using the Dashboard<a name="use-aggregated-view"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the navigation pane, choose **Aggregators**, and then review your rules and their compliance states; AWS resources and their configuration data\. You can do the following:
   + Choose an aggregator from the dashboard and filter through your aggregators by AWS region, or account ID\.
   + View the top ten resource types, in the descending order according to the number of resources\. Choose view all resources to go to the **Aggregated resources** page\. On this page, you can view all the aggregated resources for an account\.
   + View the top five accounts by the number of resources, in the descending order according to the number of resources\. Choose the number of resources for an account to go to the **Aggregated Resources** page\. On this page, you can view all the aggregated resources for an account\.
   + View the top five noncompliant rules, in descending order according to the number of noncompliant resources\. Choose a rule to go to the **Rule details** page\.
   + View the top five accounts by noncompliant rules, in descending order according to the number of noncompliant rules\. Choose an account to go to the **Aggregated Rules** page\. On this page, you can view all the aggregated rules for an account\.

**Note**  
Data displayed on the tiles is subject to delays\.  
The **Data collection from all source accounts and regions is incomplete** message is displayed in the aggregated view for the following reasons:  
AWS Config noncompliant rules and configuration data of AWS resources transfer is in progress\.
AWS Config can't find rules to match the filter\. Select the appropriate account or region and try again\.
The **Data collection from your organization is incomplete\. You can view the below data only for 24 hours\.** message is displayed in the aggregated view for the following reasons:  
AWS Config is unable to access your organization details due to invalid IAM role\. If the IAM role is invalid for more than 24 hours, AWS Config deletes data for entire organization\.
AWS Config service access is disabled in your organization\.

## Learn More<a name="learn-more-setup-console"></a>
+ [Concepts](config-concepts.md)
+ [Viewing Configuration and Compliance Data in the Aggregator Dashboard](#viewing-the-aggregate-dashboard)
+ [Setting Up an Aggregator Using the Console](setup-aggregator-console.md)
+ [Authorizing Aggregator Accounts to Collect AWS Config Configuration and Compliance Data Using the Console](authorize-aggregator-account-console.md)
+ [Troubleshooting for Multi\-Account Multi\-Region Data Aggregation](aggregate-data-troubleshooting.md)