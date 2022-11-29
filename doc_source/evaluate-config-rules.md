# Evaluation Mode and Trigger Types for AWS Config Rules<a name="evaluate-config-rules"></a>

When you add a rule to your account, you can specify when in the resource creation and management process that you want AWS Config to evaluate your resources\. This is the *evaluation mode*\.

Depending on the rule, AWS Config can evaluate your resource configurations before a resource has been provisioned, after a resource has been provisioned, or both\. Evaluating a resource pre\-provisioning is **proactive evaluation**\. Evaluating a resource post\-provisioning is **detective evaluation**\.

## Evaluation modes<a name="aws-config-rules-evaluation-modes"></a>

There are two evaluation modes:

**Proactive**  
Use proactive evaluation to evaluate resources before resource provisioning\. This allows you to evaluate the configuration settings of your resources before they are created or updated\. 

**Detective**  
Use detective evaluation to evaluate resources that have already been provisioned\. This allows you to evaluate the configuration settings of your existing resources\.

## Proactive rules<a name="aws-config-rules-proactive-rules"></a>

### Trigger type<a name="w2aac12c28b9b3"></a>

For proactive evaluation, there is only one type of trigger: **Configuration changes**\.

AWS Config runs evaluations for the rule when there are any recorded pre\-provisioned resource changes\.

### Example rule with proactive evaluation<a name="example-evaluation-modes"></a>

**Example change\-triggered rule**

1. You add the AWS Config managed rule, `S3_BUCKET_LOGGING_ENABLED`, to your account to check if your S3 buckets have logging enabled\.

1. For the evaluation mode, choose **Turn on proactive evaluation** in the AWS Management Console, or enable `PROACTIVE` for `EvaluationModes` in the [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html) API\. For more information, see [Managing Your AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_manage-rules.html)\.

1. AWS Config evaluates if a bucket in your account does not have logging enabled before it has been deployed to production\.

### List of managed rules with proactive evaluation<a name="list-proactive-rules"></a>

Currently, the following managed rules support proactive evaluation:
+ [api\-gw\-xray\-enabled](https://docs.aws.amazon.com/config/latest/developerguide/api-gw-xray-enabled.html)
+ [autoscaling\-group\-elb\-healthcheck\-required](https://docs.aws.amazon.com/config/latest/developerguide/autoscaling-group-elb-healthcheck-required.html)
+ [eip\-attached](https://docs.aws.amazon.com/config/latest/developerguide/eip-attached.html)
+ [elasticsearch\-logs\-to\-cloudwatch](https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-logs-to-cloudwatch.html)
+ [elasticsearch\-node\-to\-node\-encryption\-check](https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-node-to-node-encryption-check.html)
+ [lambda\-function\-settings\-check](https://docs.aws.amazon.com/config/latest/developerguide/lambda-function-settings-check.html)
+ [lambda\-inside\-vpc](https://docs.aws.amazon.com/config/latest/developerguide/lambda-inside-vpc.html)
+ [rds\-automatic\-minor\-version\-upgrade\-enabled](https://docs.aws.amazon.com/config/latest/developerguide/rds-automatic-minor-version-upgrade-enabled.html)
+ [rds\-enhanced\-monitoring\-enabled](https://docs.aws.amazon.com/config/latest/developerguide/rds-enhanced-monitoring-enabled.html)
+ [rds\-instance\-public\-access\-check](https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html)
+ [rds\-multi\-az\-support](https://docs.aws.amazon.com/config/latest/developerguide/rds-multi-az-support.html)
+ [ rds\-storage\-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/ rds-storage-encrypted.html)
+ [redshift\-cluster\-maintenancesettings\-check](https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-maintenancesettings-check.html)
+ [redshift\-cluster\-public\-access\-check](https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-public-access-check.html)
+ [s3\-bucket\-logging\-enabled](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-logging-enabled.html)
+ [sns\-encrypted\-kms](https://docs.aws.amazon.com/config/latest/developerguide/sns-encrypted-kms.html)
+ [subnet\-auto\-assign\-public\-ip\-disabled](https://docs.aws.amazon.com/config/latest/developerguide/subnet-auto-assign-public-ip-disabled.html)

## Detective rules<a name="aws-config-rules-detective-rules"></a>

### Trigger types<a name="w2aac12c28c11b3"></a>

For detective evaluation, there are two types of triggers:

**Configuration changes**  
AWS Config runs evaluations for the rule when certain types of post\-provisioned resources are created, changed, or deleted\.  
You choose which resources initiate the evaluation by defining the rule's *scope*\. The scope can include the following:  
+ One or more resource types
+ A combination of a resource type and a resource ID
+ A combination of a tag key and value
+ When any recorded resource is created, updated, or deleted
AWS Config runs the evaluation when it detects a change to a resource that matches the rule's scope\. You can use the scope to constrain which resources initiate evaluations\. Otherwise, evaluations are initiated when there are any recorded post\-provisioned resource changes\.

**Periodic**  
AWS Config runs evaluations for the rule at a frequency that you choose; for example, every 24 hours\.

**Hybrid**  
Some rules have both configuration change and periodic triggers\. For these rules, AWS Config evaluates your resources when it detects a configuration change and also at the frequency that you specify\.   


### Example rules with detective evaluation<a name="example-triggers"></a>

**Example change\-triggered rule**

1. You add the managed rule, `S3_BUCKET_LOGGING_ENABLED`, to your account to check if your S3 buckets have logging enabled\.

1. The trigger type for the rule is configuration changes\. AWS Config runs the evaluations for the rule when an S3 bucket is created, changed, or deleted\. 

1. When a bucket is updated, the configuration change initiates the rule and AWS Config evaluates whether the bucket is compliant against the rule\.

**Example periodic rule**

1. You add the managed rule, `IAM_PASSWORD_POLICY`, to your account\. The rule checks if the password policy for your IAM users comply with your account policy, such as requiring a minimum length or requiring specific characters\. 

1. The trigger type for the rule is periodic\. AWS Config runs evaluation for the rule at a frequency that you specify, such as every 24 hours\. 

1. Every 24 hours, the rule is initiated and AWS Config evaluates whether the passwords for your IAM users are compliant against the rule\. 

**Example hybrid rule with both configuration change and periodic triggers**

1. Create a custom rule that evaluates whether AWS CloudTrail trails in your account are turned on and logging for all Regions\.

1. You want AWS Config to run evaluations for the rule every time a trail is created, updated, or deleted\. You also want AWS Config to run the rule every 12 hours\.

1. For the trigger type, you write logic for both configuration change and periodic triggers\. For more information, see [Components of an AWS Config Rule: Writing Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_writing-rules)\.

## Rule evaluations when the configuration recorder is turned off<a name="turning-off-configuration-recorder"></a>

If you turn off the configuration recorder, AWS Config stops recording changes to your resource configurations\. This affects your rule evaluations in the following ways:
+ Periodic rules continue to run evaluations at the specified frequency\. 
+ Change\-triggered rules do not run evaluations\.
+ Hybrid rules run evaluations only at the specified frequency\. The rules do not run evaluations for configuration changes\. 
+ If you run an on\-demand evaluation for a rule with a configuration change trigger, the rule evaluates the last known state of the resource, which is the last recorded configuration item\. 