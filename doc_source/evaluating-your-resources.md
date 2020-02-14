# Evaluating Your Resources<a name="evaluating-your-resources"></a>

When you create custom rules or use managed rules, AWS Config evaluates your resources against those rules\. You can run on\-demand evaluations for resources against your rules\. For example, this is helpful when you create a custom rule and want to verify that AWS Config is correctly evaluating your resources or to identify if there is an issue with the evaluation logic of your AWS Lambda function\. 

**Example**

1.  You create a custom rule that evaluates whether your IAM users have active access keys\. 

1.  AWS Config evaluates the resources against your custom rule\.

1.  An IAM user who doesn't have an active access key exists in your account\. Your rule doesn't correctly flag this resource as noncompliant\. 

1.  You fix the rule and start the evaluation again\. 

1. Because you fixed your rule, the rule correctly evaluates your resources, and flags the IAM user resource as noncompliant\. 

## Evaluating your Resources \(Console\)<a name="evaluating-your-resources-console"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the region selector is set to a region that supports AWS Config rules\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\.

1. In the navigation pane, choose **Rules**\. The **Rules** page shows your rules and the compliance status for each\.

1. Choose a rule from the list\.

1.  In the **Re\-evaluate rule** section, choose **Re\-evaluate**\. 

1.  AWS Config starts evaluating the resources against your rule\. 

**Note**  
You can re\-evaluate a rule once per minute\. You must wait for AWS Config to complete the evaluation for your rule before you start another evaluation\. You can't run an evaluation if at the same time the rule is being updated or if the rule is being deleted\.

## Evaluating your Resources \(CLI\)<a name="evaluating-your-resources-cli"></a>
+ Use the start\-config\-rules\-evaluation command\. 

  ```
  $ aws configservice start-config-rules-evaluation --config-rule-names ConfigRuleName
  ```

  AWS Config starts evaluating the recorded resource configurations against your rule\.

  You can also specify multiple rules in your request\.

  ```
  aws configservice start-config-rules-evaluation --config-rule-names ConfigRuleName1 ConfigRuleName2 ConfigRuleName3
  ```

## Evaluating your Resources \(API\)<a name="evaluating-your-resources-api"></a>

Use the [StartConfigRulesEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigRulesEvaluation.html) action\.