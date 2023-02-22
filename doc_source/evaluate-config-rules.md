# Evaluation Mode and Trigger Types for AWS Config Rules<a name="evaluate-config-rules"></a>

When you add a rule to your account, you can specify when in the resource creation and management process that you want AWS Config to evaluate your resources\. The resource creation and management process is known as resource provisioning\. You choose the *evaluation mode* to specify when in this process you want AWS Config to evaluate your resources\.

Depending on the rule, AWS Config can evaluate your resource configurations before a resource has been deployed, after a resource has been deployed, or both\. Evaluating a resource before it has been deployed is **proactive evaluation**\. Evaluating a resource after it has been deployed is **detective evaluation**\.

You can also choose the *trigger type* to specify how often your AWS Config rules evaluate your resources\. Resources can be evaluated when there are configuration changes, on a periodic schedule, or both\.

## Trigger types<a name="aws-config-rules-trigger-types"></a>

After you add a rule to your account, AWS Config compares your resources to the conditions of the rule\. After this initial evaluation, AWS Config continues to run evaluations each time one is triggered\. The evaluation triggers are defined as part of the rule, and they can include the following types:

**Configuration changes**  
AWS Config runs evaluations for the rule when there is a resource that matches the rule's scope and there is a change in configuration of the resource\. The evaluation runs after AWS Config sends a configuration item change notification\.  
You choose which resources initiate the evaluation by defining the rule's *scope*\. The scope can include the following:  
+ One or more resource types
+ A combination of a resource type and a resource ID
+ A combination of a tag key and value
+ When any recorded resource is created, updated, or deleted
AWS Config runs the evaluation when it detects a change to a resource that matches the rule's scope\. You can use the scope to define which resources initiate evaluations\.

**Periodic**  
AWS Config runs evaluations for the rule at a frequency that you choose; for example, every 24 hours\.

**Hybrid**  
Some rules have both configuration change and periodic triggers\. For these rules, AWS Config evaluates your resources when it detects a configuration change and also at the frequency that you specify\.   


## Evaluation modes<a name="aws-config-rules-evaluation-modes"></a>

There are two evaluation modes:

### Proactive mode<a name="aws-config-rules-evaluation-proactive"></a>

Use proactive evaluation to evaluate resources before they have been deployed\. This allows you to evaluate whether a set of resource properties, if used to define an AWS resource, would be COMPLIANT or NON\_COMPLIANT given the set of proactive rules that you have in your account in your Region\.

The [Resource type schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html) states the properties of a resource\. You can find the resource type schema in "*AWS public extensions*" within the AWS CloudFormation registry or with the following CLI commmand:

```
aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type RESOURCE
```

For more information, see [Managing extensions through the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html#registry-view) and [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the AWS CloudFormation User Guide\.

**Note**  
Proactive rules do not remediate resources that are flagged as NON\_COMPLIANT or prevent them from being deployed\.

#### Example rule with proactive evaluation<a name="example-evaluation-modes"></a>

**Example proactive rule**

1. You add the AWS Config managed rule, `S3_BUCKET_LOGGING_ENABLED`, to your account to check if your S3 buckets have logging enabled\.

1. For the evaluation mode, choose **Turn on proactive evaluation** in the AWS Management Console, or enable `PROACTIVE` for `EvaluationModes` in the [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html) API\.

Once you have turned on proactive evaluation, you can use the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API and [GetResourceEvaluationSummary](https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceEvaluationSummary.html) API to check if a bucket in your account, which has not been deployed to production, does not have logging enabled\. This allows you to test resource configurations before you deploy and re\-evaluate if you want to deploy the resource to production\.

For example, start with the StartResourceEvaluation API:

```
aws configservice start-resource-evaluation --evaluation-mode PROACTIVE
                --resource-details '{"ResourceId":"MY_RESOURCE_ID",
                                     "ResourceType":"AWS::S3::Bucket",
                                     "ResourceConfiguration": "{\"BucketName\": \"my-bucket\", \"LoggingConfiguration\": {\"DestinationBucketName\": \"my-log-bucket\",\"LogFilePrefix\":\"my-log\"}}",
                                     "ResourceConfigurationSchemaType":"CFN_RESOURCE_SCHEMA"}'
```

You should receive the `ResourceEvaluationId` in the output:

```
{
    "ResourceEvaluationId": "MY_RESOURCE_EVALUATION_ID"
}
```

Then, use the `ResourceEvaluationId` with the GetResourceEvaluationSummary API to check the evaluation result:

```
aws configservice get-resource-evaluation-summary
    --resource-evaluation-id MY_RESOURCE_EVALUATION_ID
```

You should receive output similiar to the following:

```
{
    "ResourceEvaluationId": "MY_RESOURCE_EVALUATION_ID",
    "EvaluationMode": "PROACTIVE",
    "EvaluationStatus": {
        "Status": "SUCCEEDED"
    },
    "EvaluationStartTimestamp": "2022-11-15T19:13:46.029000+00:00",
    "Compliance": "COMPLIANT",
    "ResourceDetails": {
        "ResourceId": "MY_RESOURCE_ID",
        "ResourceType": "AWS::RESOURCE::TYPE",
        "ResourceConfiguration": "{\"BucketName\": \"my-bucket\", \"LoggingConfiguration\": {\"DestinationBucketName\": \"my-log-bucket\",\"LogFilePrefix\":\"my-log\"}}",

    }
}
```

To see additional information about the evaluation result, such as which rule flagged a resource as NON\_COMPLIANT, use the [GetComplianceDetailsByResource](https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceDetailsByResource.html) API\.

#### List of managed rules with proactive evaluation<a name="list-proactive-rules"></a>

For a list of managed rules that support proactive evaluation, see [List of AWS Config Managed Rules by Evaluation Mode](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-evaluation-mode.html)\.

### Detective mode<a name="aws-config-rules-evaluation-detective"></a>

Use detective evaluation to evaluate resources that have already been deployed\. This allows you to evaluate the configuration settings of your existing resources\.

#### Example rules with detective evaluation<a name="example-triggers"></a>

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