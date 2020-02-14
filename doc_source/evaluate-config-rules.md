# Specifying Triggers for AWS Config Rules<a name="evaluate-config-rules"></a>

When you add a rule to your account, you can specify when you want AWS Config to run the rule; this is called a *trigger*\. AWS Config evaluates your resource configurations against the rule when the trigger occurs\. 

**Contents**
+ [Trigger types](#aws-config-rules-trigger-types)
+ [Example rules with triggers](#example-triggers)
+ [Rule evaluations when the configuration recorder is turned off](#turning-off-configuration-recorder)

## Trigger types<a name="aws-config-rules-trigger-types"></a>

There are two types of triggers:

**Configuration changes**  
AWS Config runs evaluations for the rule when certain types of resources are created, changed, or deleted\.  
You choose which resources trigger the evaluation by defining the rule's *scope*\. The scope can include the following:  
+ One or more resource types
+ A combination of a resource type and a resource ID
+ A combination of a tag key and value
+ When any recorded resource is created, updated, or deleted
AWS Config runs the evaluation when it detects a change to a resource that matches the rule's scope\. You can use the scope to constrain which resources trigger evaluations\. Otherwise, evaluations are triggered when any recorded resource changes\.

**Periodic**  
AWS Config runs evaluations for the rule at a frequency that you choose \(for example, every 24 hours\)\.

If you choose configuration changes and periodic, AWS Config invokes your Lambda function when it detects a configuration change and also at the frequency that you specify\. 

## Example rules with triggers<a name="example-triggers"></a>

**Example rule with configuration change trigger**

1. You add the AWS Config managed rule, `S3_BUCKET_LOGGING_ENABLED`, to your account to check whether your Amazon S3 buckets have logging enabled\.

1. The trigger type for the rule is configuration changes\. AWS Config runs the evaluations for the rule when an Amazon S3 bucket is created, changed, or deleted\. 

1. When a bucket is updated, the configuration change triggers the rule and AWS Config evaluates whether the bucket is compliant against the rule\.

**Example rule with periodic trigger**

1. You add the AWS Config managed rule, `IAM_PASSWORD_POLICY`, to your account\. The rule checks whether the password policy for your IAM users comply with your account policy, such as requiring a minimum length or requiring specific characters\. 

1. The trigger type for the rule is periodic\. AWS Config runs evaluation for the rule at a frequency that you specify, such as every 24 hours\. 

1. Every 24 hours, the rule is triggered and AWS Config evaluates whether the passwords for your IAM users are compliant against the rule\. 

**Example rule with configuration change and periodic triggers**

1. You create a custom rule that evaluates whether CloudTrail trails in your account are turned on and logging for all regions\.

1. You want AWS Config to run evaluations for the rule every time a trail is created, updated, or deleted\. You also want AWS Config to run the rule every 12 hours\.

1. For the trigger type, choose configuration changes and periodic\.

## Rule evaluations when the configuration recorder is turned off<a name="turning-off-configuration-recorder"></a>

If you turn off the configuration recorder, AWS Config stops recording changes to your resource configurations\. This affects your rule evaluations in the following ways:
+ Rules with a periodic trigger continue to run evaluations at the specified frequency\. 
+ Rules with a configuration change trigger do not run evaluations\.
+ Rules with both trigger types run evaluations only at the specified frequency\. The rules do not run evaluations for configuration changes\. 
+ If you run an on\-demand evaluation for a rule with a configuration change trigger, the rule evaluates the last known state of the resource, which is the last recorded configuration item\. 