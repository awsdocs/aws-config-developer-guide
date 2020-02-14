# Managing your AWS Config Rules<a name="evaluate-config_manage-rules"></a>

You can use the AWS Config console, AWS CLI, and AWS Config API to view, add, and delete your rules\.

**Contents**
+ [Add, View, Update and Delete Rules \(Console\)](#managing-aws-config-rules-with-the-console)
+ [View, Update, and Delete Rules \(AWS CLI\)](#managing-aws-config-rules-with-the-CLI)
+ [View, Update, and Delete Rules \(API\)](#managing-aws-config-rules-with-the-API)

## Add, View, Update and Delete Rules \(Console\)<a name="managing-aws-config-rules-with-the-console"></a>

On the **Rules** page, you can view the rules for the region in your account\. You can also see the evaluation status for each rule\.

**To view your rules**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console, verify that the region selector is set to a region that supports AWS Config rules\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\.

1. Choose **Rules**\. The **Rules** page shows your rules and the compliance status for each\.

![\[The AWS Config rules page shows you how to view your rules.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/rules-page-10.png)

1. Choose **Add rule** to get started with creating a rule\.

1. Choose a rule name to see its settings\.

1. See the compliance status of the rule when it evaluates your resources\.

1. Choose the **Edit rule** icon \(![\[Edit rule icon.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/edit-icon.png)\) to edit the rule\.

1. Choose the refresh \(![\[Edit rule icon.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/refresh-icon.png)\) icon to reload compliance results\.

**To update a rule**

1. Choose the **Edit rule** icon \(![\[Edit rule icon.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/edit-icon.png)\) for the rule that you want to update\.

1. Modify the settings on the **Config rule** page to change your rule as needed\.

1. Choose **Save**\.

**To delete a rule**

1. Choose the **Edit rule** icon \(![\[Edit rule icon.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/edit-icon.png)\) for the rule that you want to delete\.

1. On the **Configure rule** page, choose **Delete rule**\.

1. When prompted, choose **Delete**\.

**To add a rule**

If you choose **Add rule**, you can see the available AWS managed rules on the **Add rule** page\. You can also create your own custom rule\.

1. If you want to create your own rule, choose **Add custom rule** and follow the procedure in [Developing a Custom Rule for AWS Config](evaluate-config_develop-rules_nodejs.md)\.

1. To add a managed rule, choose a rule on the page and follow the procedure in [Working with AWS Config Managed Rules](managing-aws-managed-rules.md)\.

![\[The AWS Config rules page shows how to manage your rules after set up.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/aws-config-rules-page-50.png)

On the **Add rule** page, you can do the following:

1. Choose **Add custom rule** to create your own rule\.

1. Type in the search field to filter results by rule name, description, or label\. For example, type **EC2** to return rules that evaluate EC2 resource types or type **periodic** to return rules with periodic triggers\. Type "new" to search for newly added rules\. For more information about trigger types, see [Specifying Triggers for AWS Config Rules](evaluate-config-rules.md)\.

1. Choose the arrow icon to see the next page of rules\.

1. Recently added rules are marked as **New**\.

1. See the labels to identify the resource type that the rule evaluates and if the rule has a periodic trigger\.

## View, Update, and Delete Rules \(AWS CLI\)<a name="managing-aws-config-rules-with-the-CLI"></a>

**To view your rules**
+ Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-config-rules.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-config-rules.html) command:

  ```
  $ aws configservice describe-config-rules
  ```

  AWS Config returns the details for all of your rules\.

**To update a rule**

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

**To delete a rule**
+ Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/delete-config-rule.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/delete-config-rule.html) command as shown in the following example:

  ```
  $ aws configservice delete-config-rule --config-rule-name ConfigRuleName
  ```

## View, Update, and Delete Rules \(API\)<a name="managing-aws-config-rules-with-the-API"></a>

**To view your rules**

Use the [DescribeConfigRules](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigRules.html) action\.

**To update or add a rule**

Use the [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html) action\.

**To delete a rule**

Use the [DeleteConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigRule.html) action\.

**Note**  
If a rule is creating invalid evaluation results, you might want to delete these results before you fix the rule and run a new evaluation\. For more information, see [Deleting Evaluation Results](deleting-evaluations-results.md)\.