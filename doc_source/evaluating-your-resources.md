# Evaluating Your Resources with AWS Config Rules<a name="evaluating-your-resources"></a>

When you create custom rules or use managed rules, AWS Config evaluates your resources against those rules\. You can run on\-demand evaluations for resources against your rules\. For example, this is helpful when you create a custom rule and want to check that AWS Config is correctly evaluating your resources or to identify if there is an issue with the evaluation logic of your AWS Lambda function\. 

**Example**

1.  You create a custom rule that evaluates whether your IAM users have active access keys\. 

1.  AWS Config evaluates your resources against your custom rule\.

1.  An IAM user who doesn't have an active access key exists in your account\. Your rule doesn't correctly flag this resource as NON\_COMPLIANT\. 

1.  You fix the rule and start the evaluation again\. 

1. Because you fixed your rule, the rule correctly evaluates your resources, and flags the IAM user resource as NON\_COMPLIANT\. 

When you add a rule to your account, you can specify when in the resource creation and management process that you want AWS Config to evaluate your resources\. The resource creation and management process is known as resource provisioning\. You choose the *evaluation mode* to specify when in this process you want AWS Config to evaluate your resources\.

Depending on the rule, AWS Config can evaluate your resource configurations before a resource has been deployed, after a resource has been deployed, or both\. Evaluating a resource before it has been deployed is **proactive evaluation**\. Evaluating a resource after it has been deployed is **detective evaluation**\.

## Proactive mode<a name="evaluating-your-resources-proactive"></a>

Use proactive evaluation to evaluate resources before they have been deployed\. This allows you to evaluate whether a set of resource properties, if used to define an AWS resource, would be COMPLIANT or NON\_COMPLIANT given the set of proactive rules that you have in your account in your Region\.

The [Resource type schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html) states the properties of a resource\. You can find the resource type schema in "*AWS public extensions*" within the AWS CloudFormation registry or with the following CLI commmand:

```
aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type RESOURCE
```

For more information, see [Managing extensions through the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html#registry-view) and [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the AWS CloudFormation User Guide\.

**Note**  
Proactive rules do not remediate resources that are flagged as NON\_COMPLIANT or prevent them from being deployed\.

### Evaluating your Resources<a name="evaluating-your-resources-console-proactive"></a>

**To turn on proactive evalution**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the Region selector is set to a Region that supports AWS Config rules\. For the list of supported AWS Regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\. 

1. In the left navigation, choose **Rules**\. For a list of managed rules that support proactive evaluation, see [List of AWS Config Managed Rules by Evaluation Mode](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-evaluation-mode.html)\.

1. Choose a rule, and then choose **Edit rule** for the rule that you want to update\.

1. For **Evaluation mode**, choose **Turn on proactive evaluation** to allow you to run evaluations on the configuration settings of your resources before they are deployed\.

1. Choose **Save**\.

**Note**  
You can also turn on proactive evaluation using the [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-config-rule.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-config-rule.html) command and enabling `PROACTIVE` for `EvaluationModes` or using the [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html) action and enabling `PROACTIVE` for `EvaluationModes`\.

Once you have turned on proactive evaluation, you can use the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API and [GetResourceEvaluationSummary](https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceEvaluationSummary.html) API to check if the resources you specify in these commands would be flagged as NON\_COMPLIANT by the proactive rules in your account in your Region\.

For example, start with the StartResourceEvaluation API:

```
aws configservice start-resource-evaluation --evaluation-mode PROACTIVE
                --resource-details '{"ResourceId":"MY_RESOURCE_ID",
                                     "ResourceType":"AWS::RESOURCE::TYPE",
                                     "ResourceConfiguration":"RESOURCE_DEFINITION_AS_PER_THE_RESOURCE_CONFIGURATION_SCHEMA",
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
        "ResourceConfiguration": "RESOURCE_DEFINITION_AS_PER_THE_RESOURCE_CONFIGURATION_SCHEMA"
    }
}
```

To see additional information about the evaluation result, such as which rule flagged a resource as NON\_COMPLIANT, use the [GetComplianceDetailsByResource](https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceDetailsByResource.html) API\.

## Detective mode<a name="evaluating-your-resources-detective"></a>

Use detective evaluation to evaluate resources that have already been deployed\. This allows you to evaluate the configuration settings of your existing resources\.

### Evaluating your Resources \(Console\)<a name="evaluating-your-resources-console"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, check that the region selector is set to a Region that supports AWS Config rules\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/awsconfig.html) in the *Amazon Web Services General Reference*\.

1. In the navigation pane, choose **Rules**\. The **Rules** page shows the name, associated remediation action, and compliance status of each rule\.

1. Choose a rule from the table\.

1. From the **Actions** dropdown list, choose **Re\-evaluate**\.

1.  AWS Config starts evaluating the resources against your rule\.

**Note**  
You can re\-evaluate a rule once per minute\. You must wait for AWS Config to complete the evaluation for your rule before you start another evaluation\. You can't run an evaluation if at the same time the rule is being updated or if the rule is being deleted\.

### Evaluating your Resources \(CLI\)<a name="evaluating-your-resources-cli"></a>
+ Use the start\-config\-rules\-evaluation command:

  ```
  $ aws configservice start-config-rules-evaluation --config-rule-names ConfigRuleName
  ```

  AWS Config starts evaluating the recorded resource configurations against your rule\. You can also specify multiple rules in your request:

  ```
  $ aws configservice start-config-rules-evaluation --config-rule-names ConfigRuleName1 ConfigRuleName2 ConfigRuleName3
  ```

### Evaluating your Resources \(API\)<a name="evaluating-your-resources-api"></a>

Use the [StartConfigRulesEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigRulesEvaluation.html) action\.