# Managing Your AWS Config Rules<a name="evaluate-config_manage-rules"></a>

You can use the AWS Config console, AWS CLI, and AWS Config API to view, add, and delete your rules\.

## Add, View, Update and Delete Rules \(Console\)<a name="managing-aws-config-rules-with-the-console"></a>

The **Rules** page shows your rules and their current compliance results in a table\. The result for each rule is **Evaluating\.\.\.** until AWS Config finishes evaluating your resources against the rule\. You can update the results with the refresh button\. When AWS Config finishes evaluations, you can see the rules and resource types that are compliant or noncompliant\. For more information, see [Viewing Configuration Compliance](evaluate-config_view-compliance.md)\.

**Note**  
AWS Config evaluates only the resource types that it is recording\. For example, if you add the **cloudtrail\-enabled** rule but don't record the CloudTrail trail resource type, AWS Config can't evaluate whether the trails in your account are compliant or noncompliant\. For more information, see [Selecting Which Resources AWS Config Records](select-resources.md)\.

### Adding rules<a name="add-rules-console"></a>

**To add a rule**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the region selector is set to a region that supports AWS Config rules\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\. 

1. In the left navigation, choose **Rules**\. 

1. On the **Rules** page, choose **Add rule**\. 

1. On the **Specify rule type** page, specify the rule type by completing the following steps:

   1. Type in the search field to filter the list of managed rules by rule name, description, and label\. For example, type **EC2** to return rules that evaluate EC2 resource types or type **periodic** to return rules that are triggered periodically\.

   1. You can also create your own custom rule\. Choose **Create custom rule using Lambda** or **Create custom rule using Guard**, and follow the procedure in [Creating AWS Config Custom Lambda Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_lambda-functions.html) or [Creating AWS Config Custom Policy Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_cfn-guard.html)\. 

1. On the **Configure rule** page, configure your rule by completing the following steps:

   1. For **Name**, type a unique name for the rule\.

   1. For **Description**, type a description for the rule\.

   1. For **Evaluation mode**, choose when in the resource creation and management process you want AWS Config to evaluate your resources\. Depending on the rule, AWS Config can evaluate your resource configurations before a resource has been deployed, after a resource has been deployed, or both\.

      1. Choose **Turn on proactive evaluation** to allow you to run evaluations on the configuration settings of your resources before they are deployed\.

         Once you have turned on proactive evaluation, you can use the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API and [GetResourceEvaluationSummary](https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceEvaluationSummary.html) API to check if the resources you specify in these commands would be flagged as NON\_COMPLIANT by the proactive rules in your account in your Region\.

          For more information on using this commands, see [Evaluating Your Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluating-your-resources.html#evaluating-your-resources-proactive)\. For a list of managed rules that support proactive evaluation, see [List of AWS Config Managed Rules by Evaluation Mode](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-evaluation-mode.html)\.

      1. Choose **Turn on detective evaluation** to evaluate the configuration settings of your existing resources\.

         For detective evaluation, there are two types of triggers: **When configuration changes** and **Periodic**\.

         1.  If the trigger types for your rule include **Configuration changes**, specify one of the following options for **Scope of changes** with which AWS Config invokes your Lambda function:
            +  **Resources** – When a resource that matches the specified resource type, or the type plus identifier, is created, changed, or deleted\.
            +  **Tags** – When a resource with the specified tag is created, changed, or deleted\.
            +  **All changes** – When a resource recorded by AWS Config is created, changed, or deleted\.

            AWS Config runs the evaluation when it detects a change to a resource that matches the rule's scope\. You can use the scope to define which resources initiate evaluations\.

         1. If the trigger types for your rule include **Periodic**, specify the **Frequency** with which AWS Config invokes your Lambda function\.

   1. For **Parameters**, you can customize the values for the provided keys if your rule includes parameters\. A parameter is an attribute that your resources must adhere to before they are considered compliant with the rule\.

1. On the **Review and create** page, review all your selections before adding the rule to your AWS account\. If your rule is not working as expected, you might see one of the following for **Compliance**: 
   +  **No results reported** \- AWS Config evaluated your resources against the rule\. The rule did not apply to the AWS resources in its scope, the specified resources were deleted, or the evaluation results were deleted\. To get evaluation results, update the rule, change its scope, or choose **Re\-evaluate**\. 

     This message may also appear if the rule didn't report evaluation results\.
   +  **No resources in scope ** \- AWS Config cannot evaluate your recorded AWS resources against this rule because none of your resources are within the rule’s scope\. To get evaluation results, edit the rule and change its scope, or add resources for AWS Config to record by using the **Settings** page\.
   +  **Evaluations failed** \- For information that can help you determine the problem, choose the rule name to open its details page and see the error message\.

### Viewing rules<a name="view-rules-console"></a>

**To view your rules**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the region selector is set to a region that supports AWS Config rules\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\. 

1. In the left navigation, choose **Rules**\. 

1. The **Rules** page shows all the rule that are currently in your AWS account\. It lists the name, associated remediation action, and compliance status of each rule\.
   + Choose **Add rule** to get started with creating a rule\.
   + Choose a rule to see its settings, or choose a rule and **View details**\.
   + See the compliance status of the rule when it evaluates your resources\.
   + Choose a rule and **Edit rule** to change the configuration settings of the rule and set a remediation action for a noncompliant rule\.

### Updating rules<a name="update-rules-console"></a>

**To update a rule**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the region selector is set to a region that supports AWS Config rules\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\. 

1. In the left navigation, choose **Rules**\. 

1. Choose a rule and **Edit rule** for the rule that you want to update\.

1. Modify the settings on the **Edit rule** page to change your rule as needed\.

1. Choose **Save**\.

### Deleting rules<a name="delete-rules-console"></a>

**To delete a rule**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the region selector is set to a region that supports AWS Config rules\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\. 

1. In the left navigation, choose **Rules**\. 

1. Choose a rule from the table that you want to delete\.

1. From the **Actions** dropdown list, choose **Delete rule**\.

1. When prompted, type "Delete" \(case\-sensitive\) and then choose **Delete**\.

### Turning on proactive evaluation<a name="turn-on-proactive-rules-console"></a>

You can use *proactive evaluation* to evaluate resources before they have been deployed\. This allows you to evaluate whether a set of resource properties, if used to define an AWS resource, would be COMPLIANT or NON\_COMPLIANT given the set of proactive rules that you have in your account in your Region\.

The [Resource type schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html) states the properties of a resource\. You can find the resource type schema in "*AWS public extensions*" within the AWS CloudFormation registry or with the following CLI commmand:

```
aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type RESOURCE
```

For more information, see [Managing extensions through the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html#registry-view) and [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the AWS CloudFormation User Guide\.

**Note**  
Proactive rules do not remediate resources that are flagged as NON\_COMPLIANT or prevent them from being deployed\.

**To turn on proactive evalution**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the Region selector is set to a Region that supports AWS Config rules\. For the list of supported AWS Regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\. 

1. In the left navigation, choose **Rules**\. For a list of managed rules that support proactive evaluation, see [List of AWS Config Managed Rules by Evaluation Mode](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-evaluation-mode.html)\.

1. Choose a rule, and then choose **Edit rule** for the rule that you want to update\.

1. For **Evaluation mode**, choose **Turn on proactive evaluation** to allow you to run evaluations on the configuration settings of your resources before they are deployed\.

1. Choose **Save**\.

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

## View, Update or Add, and Delete Rules \(AWS CLI\)<a name="managing-aws-config-rules-with-the-CLI"></a>

### Viewing rules<a name="view-rules-cli"></a>

**To view your rules**
+ Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-config-rules.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-config-rules.html) command:

  ```
  $ aws configservice describe-config-rules
  ```

  AWS Config returns the details for all of your rules\.

### Updating or adding rules<a name="update-rules-cli"></a>

**To update or add a rule**

1. Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-config-rule.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-config-rule.html) command with the `--generate-cli-skeleton` parameter to create a local JSON file that has the parameters for your rule:

   ```
   $ aws configservice put-config-rule --generate-cli-skeleton > putConfigRule.json
   ```

1. Open the JSON file in a text editor and remove any parameters that don't need updating, with the following exceptions:
   + Include at least one of the following parameters to identify the rule: 

     `ConfigRuleName`, `ConfigRuleArn`, or `ConfigRuleId`\.
   + If you are updating a custom rule, you must include the `Source` object and its parameters\.

1. Fill in the values for the parameters that remain\. To reference the details of your rule, use the describe\-config\-rules command\.

   For example, the following JSON code updates the resource types that are in the scope of a custom rule:

   ```
   {
     "ConfigRule": {
       "ConfigRuleName": "ConfigRuleName",
       "Scope": {
         "ComplianceResourceTypes": [
           "AWS::EC2::Instance",
           "AWS::EC2::Volume",
           "AWS::EC2::VPC"
         ]
       },
       "Source": {
         "Owner": "CUSTOM_LAMBDA",
         "SourceIdentifier": "arn:aws:lambda:us-east-2:123456789012:function:ConfigRuleName",
         "SourceDetails": [
           {
             "EventSource": "aws.config",
             "MessageType": "ConfigurationItemChangeNotification"
           }
         ]
       }
     }
   }
   ```

1. Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-config-rule.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-config-rule.html) command with the `--cli-input-json` parameter to pass your JSON configuration to AWS Config:

   ```
   $ aws configservice put-config-rule --cli-input-json file://putConfigRule.json
   ```

1. To verify that you successfully updated your rule, use the describe\-config\-rules command to view the rule's configuration:

   ```
   $ aws configservice describe-config-rules --config-rule-name ConfigRuleName
   {
       "ConfigRules": [
           {
               "ConfigRuleState": "ACTIVE",
               "ConfigRuleName": "ConfigRuleName",
               "ConfigRuleArn": "arn:aws:config:us-east-2:123456789012:config-rule/config-rule-nnnnnn",
               "Source": {
                   "Owner": "CUSTOM_LAMBDA",
                   "SourceIdentifier": "arn:aws:lambda:us-east-2:123456789012:function:ConfigRuleName",
                   "SourceDetails": [
                       {
                           "EventSource": "aws.config",
                           "MessageType": "ConfigurationItemChangeNotification"
                       }
                   ]
               },
               "Scope": {
                   "ComplianceResourceTypes": [
                       "AWS::EC2::Instance",
                       "AWS::EC2::Volume",
                       "AWS::EC2::VPC"
                   ]
               },
               "ConfigRuleId": "config-rule-nnnnnn"
           }
       ]
   }
   ```

### Deleting rules<a name="delete-rules-cli"></a>

**To delete a rule**
+ Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/delete-config-rule.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/delete-config-rule.html) command as shown in the following example:

  ```
  $ aws configservice delete-config-rule --config-rule-name ConfigRuleName
  ```

### Turning on proactive evaluation<a name="turn-on-proactive-rules-cli"></a>

You can use *proactive evaluation* to evaluate resources before they have been deployed\. This allows you to evaluate whether a set of resource properties, if used to define an AWS resource, would be COMPLIANT or NON\_COMPLIANT given the set of proactive rules that you have in your account in your Region\.

The [Resource type schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html) states the properties of a resource\. You can find the resource type schema in "*AWS public extensions*" within the AWS CloudFormation registry or with the following CLI commmand:

```
aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type RESOURCE
```

For more information, see [Managing extensions through the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html#registry-view) and [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the AWS CloudFormation User Guide\.

**Note**  
Proactive rules do not remediate resources that are flagged as NON\_COMPLIANT or prevent them from being deployed\.

**To turn on proactive evaluation**

Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-config-rule.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-config-rule.html) command and enable `PROACTIVE` for `EvaluationModes`\.

Once you have turned on proactive evaluation, you can use the [start\-resource\-evaluation](https://docs.aws.amazon.com/cli/latest/reference/configservice/start-resource-evaluation.html) CLI command and [get\-resource\-evaluation\-summary](https://docs.aws.amazon.com/cli/latest/reference/configservice/get-resource-evaluation-summary.html) CLI command to check if the resources you specify in these commands would be flagged as NON\_COMPLIANT by the proactive rules in your account in your Region\.

For example, start with the start\-resource\-evaluation command:

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

Then, use the `ResourceEvaluationId` with the get\-resource\-evaluation\-summary to check the evaluation result:

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

To see additional information about the evaluation result, such as which rule flagged a resource as NON\_COMPLIANT, use the [get\-compliance\-details\-by\-resource](https://docs.aws.amazon.com/cli/latest/reference/configservice/get-compliance-details-by-resource.html) CLI command\.

**Note**  
For a list of managed rules that support proactive evaluation, see [List of AWS Config Managed Rules by Evaluation Mode](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-evaluation-mode.html)\.

## View, Update or Add, and Delete Rules \(API\)<a name="managing-aws-config-rules-with-the-API"></a>

**To view your rules**

Use the [DescribeConfigRules](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigRules.html) action\.

**To update or add a rule**

Use the [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html) action\.

**To delete a rule**

Use the [DeleteConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigRule.html) action\.

**Note**  
If a rule is creating evaluation results that are not valid, it is recommended that to delete these results before you fix the rule and run a new evaluation\. For more information, see [Deleting Evaluation Results from AWS Config Rules](deleting-evaluations-results.md)\.

### Turning on proactive evaluation<a name="turn-on-proactive-rules-api"></a>

You can use *proactive evaluation* to evaluate resources before they have been deployed\. This allows you to evaluate whether a set of resource properties, if used to define an AWS resource, would be COMPLIANT or NON\_COMPLIANT given the set of proactive rules that you have in your account in your Region\.

The [Resource type schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html) states the properties of a resource\. You can find the resource type schema in "*AWS public extensions*" within the AWS CloudFormation registry or with the following CLI commmand:

```
aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type RESOURCE
```

For more information, see [Managing extensions through the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html#registry-view) and [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the AWS CloudFormation User Guide\.

**Note**  
Proactive rules do not remediate resources that are flagged as NON\_COMPLIANT or prevent them from being deployed\.

**To turn on proactive evaluation for a rule**

Use the [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html) action and enable `PROACTIVE` for `EvaluationModes`\.

Once you have turned on proactive evaluation, you can use the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API and [GetResourceEvaluationSummary](https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceEvaluationSummary.html) API to check if the resources you specify in these commands would be flagged as NON\_COMPLIANT by the proactive rules in your account in your Region\. For example, start with the StartResourceEvaluation API:

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

**Note**  
For a list of managed rules that support proactive evaluation, see [List of AWS Config Managed Rules by Evaluation Mode](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-evaluation-mode.html)\.

## Sending Rule Evaluations to Security Hub<a name="setting-up-aws-config-rules-with-console-integration"></a>

After adding an AWS Config rule, you can also send rule evaluations to AWS Security Hub\. The integration between AWS Config and Security Hub allows you to triage and remediate rule evaluations alongside other misconfigurations and security issues\.

### Send Rule Evaluations to Security Hub<a name="w2aac12c39c11b5"></a>

To send rule evaluations to Security Hub, you must first set up AWS Security Hub and AWS Config, and then add at least one AWS Config managed or custom rule\. After this, AWS Config immediately starts sending rule evaluations to Security Hub\. Security Hub enriches the rule evaluations and transforms them into Security Hub findings\.

For more information about this integration, see [Available AWS Service Integrations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-internal-providers.html#integration-config) in the AWS Security Hub User Guide\.