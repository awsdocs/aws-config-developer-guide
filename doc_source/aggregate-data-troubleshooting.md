# Troubleshooting for Multi\-Account Multi\-Region Data Aggregation<a name="aggregate-data-troubleshooting"></a>

AWS Config might not aggregate data from source accounts for one of the following reasons:


****  

| If this happens | Do this | 
| --- | --- | 
| AWS Config is not enabled in the source account\. | Enable AWS Config in the source account and authorize the aggregator account to collect data\. | 
| Authorization is not granted to an aggregator account\. | Sign in to the source account and grant authorization to the aggregator account to collect AWS Config data\. | 
| There might be a temporary issue that is preventing data aggregation\. | Data aggregation is subject to delays\. Wait for a few minutes\. | 

AWS Config might not aggregate data from an organization for one of the following reasons:


****  

| If this happens | Do this | 
| --- | --- | 
| AWS Config is unable to access your organization details due to invalid IAM role\. | Create an IAM role or select a valid IAM role from the IAM role list\. If the IAM role is invalid for more than 24 hours, AWS Config deletes data for entire organization\.  | 
| AWS Config service access is disabled in your organization\. | You can enable integration between AWS Config and AWS Organizations through the EnableAWSServiceAccess API\. If you choose Add my organization in console, AWS Config automatically enables the integration between AWS Config and AWS Organizations\. | 
| AWS Config is unable to access your organization details because all features is not enabled in your organization\. | [Enable all features](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in AWS Organizations console\. | 
| Organizational changes such as adding an account, removing an account, enabling service access, and disabling service access are not upadated in Middle East \(Bahrain\) and Asia Pacific \(Hong Kong\) regions immediately\. | Organizational changes are subject to 2 hour delay\. Wait for 2 hours to see all organization changes\. | 

## Learn More<a name="learn-more-setup-console"></a>
+ [Concepts](config-concepts.md)
+ [Setting Up an Aggregator Using the Console](setup-aggregator-console.md)
+ [Authorizing Aggregator Accounts to Collect AWS Config Configuration and Compliance Data Using the Console](authorize-aggregator-account-console.md)
+ [Viewing Configuration and Compliance Data in the Aggregated View](viewing-the-aggregate-dashboard.md)