# Enabling AWS Config Rules Across all Accounts in Your Organization<a name="config-rule-multi-account-deployment"></a>

AWS Config allows you to manage AWS Config rules across all AWS accounts within an organization\. You can:
+ Centrally create, update, and delete AWS Config rules across all accounts in your organization\. 
+ Deploy a common set of AWS Config rules across all accounts and specify accounts where AWS Config rules should not be created\.
+ Use the APIs from the master account in AWS Organizations to enforce governance by ensuring that the underlying AWS Config rules are not modifiable by your organization’s member accounts\.

**Note**  
AWS Config is a regional service and the API call to deploy rules and conformance packs across accounts is region specific\. At the organization level, you need to change the context of your API call to a different region if you want to deploy rules in other regions\.

Ensure AWS Config recording is on before you use the following APIs to manage AWS Config rules across all AWS accounts within an organization:
+ [PutOrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html), adds or updates organization config rule for your entire organization evaluating whether your AWS resources comply with your desired configurations\.
+ [PutOrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html), deploys conformance packs across member accounts in an AWS Organization\.
+ [DescribeOrganizationConfigRules](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConfigRules.html), returns a list of organization config rules\.
+ [GetOrganizationConfigRuleDetailedStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_GetOrganizationConfigRuleDetailedStatus.html), returns detailed status for each member account within an organization for a given organization config rule\.
+ [DescribeOrganizationConfigRuleStatuses](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConfigRuleStatuses.html), provides organization config rule deployment status for an organization\.
+ [DeleteOrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteOrganizationConfigRule.html), deletes the specified organization config rule and all of its evaluation results from all member accounts in that organization\.