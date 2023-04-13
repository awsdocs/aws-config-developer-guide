# Managing AWS Config Rules Across All Accounts in Your Organization<a name="config-rule-multi-account-deployment"></a>

AWS Config allows you to manage AWS Config rules across all AWS accounts within an organization\. You can:
+ Centrally create, update, and delete AWS Config rules across all accounts in your organization\. 
+ Deploy a common set of AWS Config rules across all accounts and specify accounts where AWS Config rules should not be created\.
+ Use the APIs from the management account in AWS Organizations to enforce governance by ensuring that the underlying AWS Config rules are not modifiable by your organization’s member accounts\.

**Note**  
**For deployments across different regions**  
The API call to deploy rules and conformance packs across accounts is region specific\. At the organization level, you need to change the context of your API call to a different region if you want to deploy rules in other regions\. For example, to deploy a rule in US East \(N\. Virginia\), change the region to US East \(N\. Virginia\) and then call `PutOrganizationConfigRule`\.  
**For accounts within an organization**  
If a new account joins an organization, the rule or conformance pack is deployed to that account\. When an account leaves an organization, the rule or conformance pack is removed\.  
If you deploy an organizational rule or conformance pack in an organization administrator account, and then establish a delegated administrator and deploy an organizational rule or conformance pack in the delegated administrator account, you won't be able to see the organizational rule or conformance pack in the organization administrator account from the delegated administrator account or see the organizational rule or conformance pack in the delegated administrator account from organization administrator account\. The [DescribeOrganizationConfigRules](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConfigRules.html) and [DescribeOrganizationConformancePacks](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConformancePacks.html) APIs can only see and interact with the organization\-related resource that were deployed from within the account calling those APIs\.   
**Retry mechanism for new accounts added to an organization**  
Deployment of existing organizational rules and conformance packs will only be retried for 7 hours after an account is added to your organization if a recorder is not available\. You are expected to create a recorder if one doesn't exist within 7 hours of adding an account to your organization\.

Ensure AWS Config recording is on before you use the following APIs to manage AWS Config rules across all AWS accounts within an organization:
+ [PutOrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html), adds or updates organization config rule for your entire organization evaluating whether your AWS resources comply with your desired configurations\.
+ [DescribeOrganizationConfigRules](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConfigRules.html), returns a list of organization config rules\.
+ [GetOrganizationConfigRuleDetailedStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_GetOrganizationConfigRuleDetailedStatus.html), returns detailed status for each member account within an organization for a given organization config rule\.
+ [GetOrganizationCustomRulePolicy](https://docs.aws.amazon.com/config/latest/APIReference/API_GetOrganizationCustomRulePolicy.html), returns the policy definition containing the logic for your organization config custom policy rule\.
+ [DescribeOrganizationConfigRuleStatuses](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConfigRuleStatuses.html), provides organization config rule deployment status for an organization\.
+ [DeleteOrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteOrganizationConfigRule.html), deletes the specified organization config rule and all of its evaluation results from all member accounts in that organization\.

## Region Support<a name="region-support-org-config-rules"></a>

Deploying AWS Config Rules across member accounts in an AWS Organization is supported in the following Regions\.


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html)