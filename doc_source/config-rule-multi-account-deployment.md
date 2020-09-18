# Enabling AWS Config Rules Across all Accounts in Your Organization<a name="config-rule-multi-account-deployment"></a>

AWS Config allows you to manage AWS Config rules across all AWS accounts within an organization\. You can:
+ Centrally create, update, and delete AWS Config rules across all accounts in your organization\. 
+ Deploy a common set of AWS Config rules across all accounts and specify accounts where AWS Config rules should not be created\.
+ Use the APIs from the master account in AWS Organizations to enforce governance by ensuring that the underlying AWS Config rules are not modifiable by your organization’s member accounts\.

**Note**  
AWS Config is a regional service and the API call to deploy rules and conformance packs across accounts is region specific\. At the organization level, you need to change the context of your API call to a different region if you want to deploy rules in other regions\.

Ensure AWS Config recording is on before you use the following APIs to manage AWS Config rules across all AWS accounts within an organization:
+ [PutOrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html)
+ [PutOrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html)
+ [DescribeOrganizationConfigRules](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConfigRules.html)
+ [GetOrganizationConfigRuleDetailedStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_GetOrganizationConfigRuleDetailedStatus.html)
+ [DescribeOrganizationConfigRuleStatuses](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConfigRuleStatuses.html)
+ [DeleteOrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteOrganizationConfigRule.html)