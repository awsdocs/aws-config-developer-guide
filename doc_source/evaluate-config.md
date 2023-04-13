# Evaluating Resources with AWS Config Rules<a name="evaluate-config"></a>

Use AWS Config to evaluate the configuration settings of your AWS resources\. You do this by creating AWS Config rules, which represent your ideal configuration settings\. AWS Config provides customizable, predefined rules called managed rules to help you get started\. While AWS Config continuously tracks the configuration changes that occur among your resources, it checks whether these changes do not comply with the conditions in your rules\. If a resource does not comply with rule, AWS Config flags the resource and the rule as *noncompliant*\. The following are the possible evaluation results for an AWS Config rule:
+ `COMPLIANT` \- the rule passes the conditions of the compliance check\.
+ `NON_COMPLIANT` \- the rule fails the conditions of the compliance check\.
+ `ERROR` \- one of the required/optional parameters is not valid, or not of the correct type, or is formatted incorrectly\.
+ `NOT_APPLICABLE` \- used to filter out resources that the logic of the rule cannot be applied to\. 

  For example, the [alb\-desync\-mode\-check](https://docs.aws.amazon.com/config/latest/developerguide/alb-desync-mode-check.html) rule only checks Application Load Balancers, and ignores Network Load Balancers and Gateway Load Balancers\.

For example, when an EC2 volume is created, AWS Config can evaluate the volume against a rule that requires volumes to be encrypted\. If the volume is not encrypted, AWS Config flags the volume and the rule as noncompliant\. AWS Config can also check all of your resources for account\-wide requirements\. For example, AWS Config can check whether the number of EC2 volumes in an account stays within a desired total, or whether an account uses AWS CloudTrail for logging\.

**Service\-linked rules** are a unique type of managed rule that support other AWS services to create AWS Config rules in your account\. These rules are predefined to include all the permissions required to call other AWS services on your behalf\. These rules are similar to standards that an AWS service recommends in your AWS account for compliance verification\. For more information, see [Service\-Linked AWS Config Rules](service-linked-awsconfig-rules.md)\.

The AWS Config console shows the compliance status of your rules and resources\. You can see how your AWS resources comply overall with your desired configurations, and learn which specific resources are noncompliant\. You can also use the AWS CLI, the AWS Config API, and AWS SDKs to make requests to the AWS Config service for compliance information\.

By using AWS Config to evaluate your resource configurations, you can assess how well your resource configurations comply with internal practices, industry guidelines, and regulations\.

For the maximum number of AWS Config rules per Region per account and other service limits, see [AWS Config Service Limits](https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html)\.

You can also create custom rules to evaluate additional resources that AWS Config doesn't yet record\. For more information, see [AWS Config Custom Rules](evaluate-config_develop-rules.md) and [Evaluating Additional Resource Types](evaluate-config_develop-rules_nodejs.md#creating-custom-rules-for-additional-resource-types)\.

**Topics**
+ [Region Support](#region-support-config-rules)
+ [Components of an AWS Config Rule](evaluate-config_components.md)
+ [Evaluation Mode and Trigger Types for AWS Config Rules](evaluate-config-rules.md)
+ [AWS Config Managed Rules](evaluate-config_use-managed-rules.md)
+ [AWS Config Custom Rules](evaluate-config_develop-rules.md)
+ [Managing Your AWS Config Rules](evaluate-config_manage-rules.md)
+ [Evaluating Your Resources with AWS Config Rules](evaluating-your-resources.md)
+ [Deleting Evaluation Results from AWS Config Rules](deleting-evaluations-results.md)
+ [Managing AWS Config Rules Across All Accounts in Your Organization](config-rule-multi-account-deployment.md)
+ [Remediating Noncompliant Resources with AWS Config Rules](remediation.md)

## Region Support<a name="region-support-config-rules"></a>

Currently, AWS Config Rules is supported in the following regions:


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html)

Deploying AWS Config Rules across member accounts in an AWS Organization is supported in the following Regions\.


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html)