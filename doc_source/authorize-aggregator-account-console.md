# Authorizing Aggregator Accounts to Collect AWS Config Configuration and Compliance Data Using the Console<a name="authorize-aggregator-account-console"></a>

AWS Config allows you to authorize accounts to collect AWS Config configuration and compliance data\. 

On the **Authorizations** page, you can do the following:
+ Add Authorization to allow a specified aggregator account and Region to collect AWS Config configuration and compliance data from your current account\.
+ Authorize a pending request from an aggregator account to collect AWS Config configuration and compliance data from your current account\.
+ Delete an authorization for an aggregator account to collect AWS Config configuration and compliance data from your current account\.

**Topics**
+ [Add Authorization for Aggregator Accounts and Regions](#add-authorization-console)
+ [Authorize a Pending Request for an Aggregator Account](#authorization-pending-request-console)
+ [Delete Authorization for an Existing Aggregator Account](#delete-authorization-console)
+ [Learn More](#learn-more-setup-console)

## Add Authorization for Aggregator Accounts and Regions<a name="add-authorization-console"></a>

You can add authorization to grant permission to aggregator accounts and Regions to collect AWS Config configuration and compliance data\.

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Navigate to the **Authorizations** page and choose **Add authorization**\.
**Note**  
**There are two types of aggregators: Individual account aggregator and Organization aggregator**  
For an individual account aggregator, authorization is required for all source accounts and Regions that you want to include, including both external accounts and Regions and Organization member accounts and Regions\.  
For an organization aggregator, authorization is not required for Organization member account regions since authorization is integrated with the AWS Organizations service\.  
**Aggregators do not automatically enable AWS Config on your behalf**  
AWS Config needs to be enabled in the source account and Region for either type of aggregator, in order for AWS Config data to be generated in the source account and Region\.

1. For **Aggregator account**, type the 12\-digit account ID of an aggregator account\.

1. For **Aggregator region**, choose the AWS Regions where the aggregator account is allowed to collect AWS Config configuration and compliance data\.

1. Choose **Add authorization** to confirm your selection\.

   AWS Config displays an aggregator account, Region, and authorization status\.
**Note**  
You can also add authorization to aggregator accounts and Regions programatically using AWS CloudFormation sample template\. For more information, see [AWS::Config::AggregationAuthorization](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html) in the *AWS CloudFormation user guide*\.

## Authorize a Pending Request for an Aggregator Account<a name="authorization-pending-request-console"></a>

If you have a pending authorization request from an existing aggregator account you will see the request status on the **Authorizations** page\. You can authorize a pending request from this page\.

1. Choose the aggregator account that you want to authorize, and then choose **Authorize**\.

   A confirmation message is displayed to confirm that you want to grant the aggregator account permission to collect AWS Config data from this account\.

1. Choose **Authorize** again to confirm that you want to grant permission to the aggregator account\.

   The authorization status changes from **Requesting for authorization** to **Authorized**\.

**Note**  
**Authorization approval period**  
Authorization approval is required to add source accounts to an individual account aggregator\. A pending authorization approval request will be available for 7 days after an individual account aggregator adds a source account\.

## Delete Authorization for an Existing Aggregator Account<a name="delete-authorization-console"></a>

1. Choose the aggregator account that you want to delete authorization, and then choose **Delete**\.

   A warning message is displayed\. When you delete this authorization, AWS Config data will no longer be shared with the aggregator account\.
**Note**  
After authorization for an aggregator is deleted the data will remain in the aggregator account for up to 24 hours before being deleted\.

1. Choose **Delete** again to confirm your selection\.

   The aggregator account is now deleted\.

## Learn More<a name="learn-more-setup-console"></a>
+ [Concepts](config-concepts.md)
+ [Setting Up an Aggregator Using the Console](setup-aggregator-console.md)
+ [Viewing Compliance Data in the Aggregator Dashboard](viewing-the-aggregate-dashboard.md)
+ [Troubleshooting for Multi\-Account Multi\-Region Data Aggregation](aggregate-data-troubleshooting.md)