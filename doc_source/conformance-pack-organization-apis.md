# Managing Conformance Packs Across all Accounts in Your Organization<a name="conformance-pack-organization-apis"></a>

Use AWS Config to manage conformance packs across all AWS accounts within an organization\. You can do the following:
+ Centrally deploy, update, and delete conformance packs across member accounts in an organization in AWS Organizations\.
+ Deploy a common set of AWS Config rules and remediation actions across all accounts and specify accounts where AWS Config rules and remediation actions should not be created\.
+ Use the APIs from the master account in AWS Organizations to enforce governance by ensuring that the underlying AWS Config rules and remediation actions are not modifiable by your organization’s member accounts\.

**Note**  
*For deployments accross different regions*  
The API call to deploy rules and conformance packs across accounts is region specific\. At the organization level, you need to change the context of your API call to a different region if you want to deploy rules in other regions\. For example, to deploy a rule in US East \(N\. Virginia\), change the region to US East \(N\. Virginia\) and then call `PutOrganizationConfigRule`\.  
*For accounts within an organzation*  
If a new account joins an organization, the rule is deployed to that account\. When an account leaves an organization, the rule is removed\.  
*Retry mechanism for new accounts added to an organization*  
Deployment of existing organizational AWS Config Rules and organizational conformance packs will only be retried for 7 hours after an account is added to your organization if a recorder is not available\. You are expected to create a recorder if one doesn't exist within 7 hours of adding an account to your organization\.

Ensure AWS Config recording is on before you use the following APIs to manage conformance pack rules across all AWS accounts within an organization:
+ [DeleteOrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteOrganizationConformancePack.html), deletes the specified organization conformance pack and all of the config rules and remediation actions from all member accounts in that organization\.
+ [DescribeOrganizationConformancePacks](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConformancePacks.html), returns a list of organization conformance packs\.
+ [DescribeOrganizationConformancePackStatuses](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConformancePackStatuses.html), provides organization conformance pack deployment status for an organization\.
+ [GetOrganizationConformancePackDetailedStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_GetOrganizationConformancePackDetailedStatus.html), returns detailed status for each member account within an organization for a given organization conformance pack\.
+ [PutOrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html), deploys conformance packs across member accounts in an AWS Organization\.

## Region Support<a name="org-conformance-packs-regions"></a>

Deploying conformance packs across member accounts in an AWS Organization is supported in the following Regions\.


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-organization-apis.html)