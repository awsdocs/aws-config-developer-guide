# Viewing Compliance Data in the Aggregator Dashboard<a name="viewing-the-aggregate-dashboard"></a>

The dashboard on the **Aggregators** page displays the configuration data of AWS resources and provides an overview of your rules and conformance packs and their compliance states\. This dashboard only displays rules with compliance results\.

It provides the total resource count of AWS resources\. The resource types and source accounts are ranked by the highest number of resources\. It also provides a count of compliant and noncompliant rules and conformance packs\. The noncompliant rules are ranked by highest number of noncompliant resources\. The noncompliant conformance packs and source accounts are ranked by the highest number of noncompliant rules\.

After setup, AWS Config starts aggregating data from the specified source accounts into an aggregator\. It might take a few minutes for AWS Config to display the compliance status of rules on this page\.

## Using the Aggregator Dashboard<a name="use-aggregated-view"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Navigate to the **Aggregators** page\. Review your rules and their compliance states; conformance packs and their compliance states, and AWS resources and their configuration data\. You can do the following:
   + Choose an aggregator from the dashboard and filter through your aggregators by AWS region, or account ID\.
   + View the top ten resource types, in the descending order according to the number of resources\. Choose view all resources to go to the **Aggregated resources** page\. On this page, you can view all the aggregated resources for an account\.
   + View the top five accounts by the number of resources, in the descending order according to the number of resources\. Choose the number of resources for an account to go to the **Aggregated Resources** page\. On this page, you can view all the aggregated resources for an account\.
   + View the top five noncompliant rules, in descending order according to the number of noncompliant resources\. Choose a rule to go to the **Rule details** page\.
   + View the top five accounts by noncompliant rules, in descending order according to the number of noncompliant rules\. Choose an account to go to the **Aggregated Rules** page\. On this page, you can view all the aggregated rules for an account\.
   + View the top five accounts by noncompliant conformance packs, in descending order according to the number of noncompliant conformance packs\. Choose an account to go to the **Aggregated Conformance Pack** page\. On this page, you can view all the aggregated conformance packs for an account\.
**Note**  
Data displayed on the tiles is subject to delays\.  
The **Data collection from all source accounts and regions is incomplete** message is displayed in the aggregated view for the following reasons:  
AWS Config noncompliant rules and configuration data of AWS resources transfer is in progress\.
AWS Config can't find rules to match the filter\. Select the appropriate account or region and try again\.
The **Data collection from your organization is incomplete\. You can view the below data only for 24 hours\.** message is displayed in the aggregated view for the following reasons:  
AWS Config is unable to access your organization details due to invalid IAM role\. If the IAM role is invalid for more than 24 hours, AWS Config deletes data for entire organization\.
AWS Config service access is disabled in your organization\.

1. In the navigation pane, choose **Aggregators** and then choose one of the following options from the dropdown menu to go its aggregated page:
   + **Conformance packs**

     View all conformance packs that are created and linked to the different AWS accounts within your aggregator\. The **Conformance Pack** page displays a table that lists the name, Region, account ID, and compliance status of each conformance pack\. From this page, you can choose a conformance pack and **View details** for more information about its rules and resources and their compliance status\.
   + **Rules**

     View all rules that are created and linked to the different AWS accounts within your aggregator\. The **Rules** page displays a table that lists the name, compliance status, Region, and account of each rule\. From this page, you can choose a rule and **View details** for information, such as its aggregator, Region, account ID, and resources in scope\.
   + **Resources**

     View all resources that are recorded and linked to the different AWS accounts within your aggregator\. From the **Resource** page, choose a resource and **View details** to view its details and the rules associated with it and the current resource configuration\. You can also see information about the resource, such as its aggregator, Region, account ID, resource name, resource type, and resource ID\.
   + **Authorizations**

     View all accounts currently authorized or pending authorization\. From the **Authorizations** page, choose **Add authorization** to provide access to another account\. Choose **Delete authorization** to revoke access from an account ID\.

## Learn More<a name="learn-more-setup-console"></a>
+ [Concepts](config-concepts.md)
+ [Viewing Compliance Data in the Aggregator Dashboard](#viewing-the-aggregate-dashboard)
+ [Setting Up an Aggregator Using the Console](setup-aggregator-console.md)
+ [Authorizing Aggregator Accounts to Collect AWS Config Configuration and Compliance Data Using the Console](authorize-aggregator-account-console.md)
+ [Troubleshooting for Multi\-Account Multi\-Region Data Aggregation](aggregate-data-troubleshooting.md)