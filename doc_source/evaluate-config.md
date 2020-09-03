# Evaluating Resources with AWS Config Rules<a name="evaluate-config"></a>

Use AWS Config to evaluate the configuration settings of your AWS resources\. You do this by creating AWS Config rules, which represent your ideal configuration settings\. AWS Config provides customizable, predefined rules called managed rules to help you get started\. You can also create your own custom rules\. While AWS Config continuously tracks the configuration changes that occur among your resources, it checks whether these changes violate any of the conditions in your rules\. If a resource violates a rule, AWS Config flags the resource and the rule as *noncompliant*\.

For example, when an EC2 volume is created, AWS Config can evaluate the volume against a rule that requires volumes to be encrypted\. If the volume is not encrypted, AWS Config flags the volume and the rule as noncompliant\. AWS Config can also check all of your resources for account\-wide requirements\. For example, AWS Config can check whether the number of EC2 volumes in an account stays within a desired total, or whether an account uses AWS CloudTrail for logging\. 

The AWS Config console shows the compliance status of your rules and resources\. You can see how your AWS resources comply overall with your desired configurations, and learn which specific resources are noncompliant\. You can also use the AWS CLI, the AWS Config API, and AWS SDKs to make requests to the AWS Config service for compliance information\.

By using AWS Config to evaluate your resource configurations, you can assess how well your resource configurations comply with internal practices, industry guidelines, and regulations\.

For regions that support AWS Config rules, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\.

You can create up to 150 AWS Config rules per region in your account\. For more information, see [AWS Config Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_config) in the *Amazon Web Services General Reference*\.

You can also create custom rules to evaluate additional resources that AWS Config doesn't yet record\. For more information, see [Evaluating Additional Resource Types](evaluate-config_develop-rules_nodejs.md#creating-custom-rules-for-additional-resource-types)\.

**Topics**
+ [Viewing Configuration Compliance](evaluate-config_view-compliance.md)
+ [Specifying Triggers for AWS Config Rules](evaluate-config-rules.md)
+ [AWS Config Managed Rules](evaluate-config_use-managed-rules.md)
+ [AWS Config Custom Rules](evaluate-config_develop-rules.md)
+ [Managing your AWS Config Rules](evaluate-config_manage-rules.md)
+ [Evaluating Your Resources](evaluating-your-resources.md)
+ [Deleting Evaluation Results](deleting-evaluations-results.md)
+ [Enabling AWS Config Rules Across all Accounts in Your Organization](config-rule-multi-account-deployment.md)
+ [Remediating Noncompliant AWS Resources by AWS Config Rules](remediation.md)
+ [Tagging Your AWS Config Resources](tagging.md)