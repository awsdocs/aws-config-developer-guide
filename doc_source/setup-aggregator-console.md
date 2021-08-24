# Setting Up an Aggregator Using the Console<a name="setup-aggregator-console"></a>

On the **Aggregator** page, you can do the following:
+ Create an aggregator by specifying the source account IDs or organization and regions from which you want to aggregate data\.
+ Edit and delete an aggregator\.

**Topics**
+ [Create an Aggregator](#add-an-aggregator-console)
+ [Edit an Aggregator](#edit-an-aggregator-console)
+ [Delete an Aggregator](#delete-an-aggregator-console)
+ [Learn More](#learn-more-setup-console)

## Create an Aggregator<a name="add-an-aggregator-console"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Navigate to the **Aggregators** page and choose **Create aggregator**\.

1. **Allow data replication**, gives permission to AWS Config to replicate data from the source accounts into an aggregator account\.

   Choose **Allow AWS Config to replicate data from source account\(s\) into an aggregator account\. You must select this checkbox to continue to add an aggregator**\.

1. For **Aggregator name**, type the name for your aggregator\.

   The aggregator name must be a unique name with a maximum of 64 alphanumeric characters\. The name can contain hyphens and underscores\.

1. For **Select source accounts**, either choose **Add individual account IDs** or **Add my organization** from which you want to aggregate data\.
**Note**  
Authorization is required when using **Add individual account IDs** to select source accounts\.
   + If you choose **Add individual account IDs**, you can add individual account IDs for an aggregator account\.

     1. Choose **Add source accounts** to add account IDs\.

     1. Choose **Add AWS account IDs** to manually add comma\-separated AWS account IDs\. If you want to aggregate data from the current account, type the account ID of the account\.

        OR

        Choose **Upload a file** to upload a file \(\.txt or \.csv\) of comma\-separated AWS account IDs\.

     1. Choose **Add source accounts** to confirm your selection\.
   + If you choose **Add my organization**, you can add all accounts in your organization to an aggregator account\.
**Note**  
You must be signed in to the management account or a registered delegated administrator and all the features must be enabled in your organization\. If the caller is a management account, AWS Config calls `EnableAwsServiceAccess` API to [enable integration](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html) between AWS Config and AWS Organizations\. If the caller is a registered delegated administrator, AWS Config calls `ListDelegatedAdministrators` API to verify whether the caller is a valid delegated administrator\.   
Ensure that the management account registers delegated administrator for AWS Config service principle name \(config\.amazonaws\.com\) before the delegated administrator creates an aggregator\. To register a delegated administrator, see [Register a Delegated Administrator](set-up-aggregator-cli.md#register-a-delegated-administrator-cli)\.

     1. Choose **Choose IAM role** to create an IAM role or choose an existing IAM role from your account\.

        You must assign an IAM role to allow AWS Config to call read\-only APIs for your organization\.

     1. Choose **Create a role** and type the IAM role name to create IAM role\.

        OR

        Choose **Choose a role from your account** to select an existing IAM role\.
**Note**  
In the IAM console, attach the `AWSConfigRoleForOrganizations` managed policy to your IAM role\. Attaching this policy allows AWS Config to call AWS Organizations `DescribeOrganization`, `ListAWSServiceAccessForOrganization`, and `ListAccounts` APIs\. By default `config.amazonaws.com` is automatically specified as a trusted entity\.

     1. Choose **Choose IAM role** to confirm your selection\.

1. For **Regions**, choose the regions for which you want to aggregate data\.
   + Select one region or multiple regions or all the AWS Regions\.
   + Select **Include future AWS Regions** to aggregate data from all future AWS Regions where multi\-account multi\-region data aggregation is enabled\.

1. Choose **Save**\. AWS Config displays the aggregator\.

## Edit an Aggregator<a name="edit-an-aggregator-console"></a>

1. To make changes to the aggregator, choose the aggregator name\.

1. Choose **Actions** and then choose **Edit**\.

1. Use the sections on the **Edit aggregator** page to change the source accounts, IAM roles, or regions for the aggregator\.
**Note**  
You cannot change source type from individual account\(s\) to organization and vice versa\.

1. Choose **Save**\.

## Delete an Aggregator<a name="delete-an-aggregator-console"></a>

1. To delete an aggregator, choose the aggregator name\.

1. Choose **Actions** and then choose **Delete**\.

   A warning message is displayed\. Deleting an aggregator results in the loss of all aggregated data\. You cannot recover this data but data in the source account\(s\) is not impacted\.

1. Choose **Delete** to confirm your selection\.

## Learn More<a name="learn-more-setup-console"></a>
+ [Concepts](config-concepts.md)
+ [Authorizing Aggregator Accounts to Collect AWS Config Configuration and Compliance Data Using the Console](authorize-aggregator-account-console.md)
+ [Viewing Compliance Data in the Aggregator Dashboard](viewing-the-aggregate-dashboard.md)
+ [Troubleshooting for Multi\-Account Multi\-Region Data Aggregation](aggregate-data-troubleshooting.md)