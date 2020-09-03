# Authorizing Aggregator Accounts to Collect AWS Config Configuration and Compliance Data Using the Console<a name="authorize-aggregator-account-console"></a>

AWS Config allows you to authorize aggregator accounts to collect AWS Config configuration and compliance data\. 

This flow is not required if you are aggregating source accounts that are part of AWS Organizations\.

On the **Authorizations** page, you can do the following:
+ Add Authorization to allow an aggregator account and region to collect AWS Config configuration and compliance data\.
+ Authorize a pending request from an aggregator account to collect AWS Config configuration and compliance data\.
+ Delete an authorization for an aggregator account\.

**Topics**
+ [Add Authorization for Aggregator Accounts and Regions](#add-authorization-console)
+ [Authorize a Pending Request for an Aggregator Account](#authorization-pending-request-console)
+ [Delete Authorization for an Exisiting Aggregator Account](#delete-authorization-console)
+ [Learn More](#learn-more-setup-console)

## Add Authorization for Aggregator Accounts and Regions<a name="add-authorization-console"></a>

You can add authorization to grant permission to aggregator accounts and regions to collect AWS Config configuration and compliance data\.

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Navigate to the **Authorizations** page and choose **Add authorization**\.

1. For **Aggregator account**, type the 12\-digit account ID of an aggregator account\.

1. For **Aggregator region**, choose the AWS regions where aggregator account is allowed to collect AWS Config configuration and compliance data\.

1. Choose **Add authorization** to confirm your selection\.

   AWS Config displays an aggregator account, region, and authorization status\.
**Note**  
You can also add authorization to aggregator accounts and regions programatically using AWS CloudFormation sample template\. For more information, see [AWS::Config::AggregationAuthorization](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html) in the *AWS CloudFormation user guide*\.

## Authorize a Pending Request for an Aggregator Account<a name="authorization-pending-request-console"></a>

If you have a pending authorization request from an exisiting aggregator account you will see the request status on the **Authorizations** page\. You can authorize a pending request from this page\.

1. For the aggregator account you want to authorize, choose **Authorize** in the Actions column\.  
![\[Authorize button requests for authorization for a pending request.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/Add_Authorization_Authorize_button.png)

   A confirmation message is displayed to confirm you grant permission to an aggregator account and region for collecting AWS Config data\.

1. Choose **Authorize** to grant this permission for an aggregator account and region\.

   The authorization status changes from **Requesting for authorization** to **Authorized**\.

## Delete Authorization for an Exisiting Aggregator Account<a name="delete-authorization-console"></a>

1. For the aggregator account you want to delete authorization, choose **Delete** in the Actions column\.

   A warning message is displayed\. When you delete this authorization, AWS Config data is not shared with an aggregator account\.
**Note**  
After authorization for an aggregator is deleted the data will remain in the aggregator account for up to 24 hours before being deleted\.

1. Choose **Delete** to confirm your selection\.

   The aggregator account is deleted\.

## Learn More<a name="learn-more-setup-console"></a>
+ [Concepts](config-concepts.md)
+ [Setting Up an Aggregator Using the Console](setup-aggregator-console.md)
+ [Viewing Configuration and Compliance Data in the Aggregated View](viewing-the-aggregate-dashboard.md)
+ [Troubleshooting for Multi\-Account Multi\-Region Data Aggregation](aggregate-data-troubleshooting.md)