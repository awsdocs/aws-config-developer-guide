# Deleting Evaluation Results<a name="deleting-evaluations-results"></a>

After AWS Config evaluates your rule, you can see the evaluation results on the **Rules** page or the **Rules details** page for the rule\. If the evaluation results are incorrect or if you want to evaluate again, you can delete the current evaluation results for the rule\. For example, if your rule was incorrectly evaluating your resources or you recently deleted resources from your account, you can delete the evaluation results and then run a new evaluation\.

## Deleting Evaluating Results \(Console\)<a name="deleting-evaluations-results-console"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the region selector is set to a region that supports AWS Config rules\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\.

1. In the navigation pane, choose **Rules**\. The **Rules** page shows your rules and the compliance status\.

1. Choose a rule from the list\.

1. In the **Delete evaluation results** section, choose **Delete results**\. AWS Config deletes the evaluation results for this rule\. 

1. When prompted, choose **Delete**\. Deleted evaluations can't be retrieved\.

1. After the evaluation results are deleted, you can manually start a new evaluation\.

## Deleting Evaluating Results \(CLI\)<a name="deleting-evaluations-results-cli"></a>
+ Use the delete\-evaluation\-results command:

  ```
  $ aws configservice delete-evaluation-results --config-rule-name ConfigRuleName
  ```

  AWS Config deletes the evaluation results for the rule\.

## Deleting Evaluating Results \(API\)<a name="deleting-evaluations-results-api"></a>

Use the [DeleteEvaluationResults](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteEvaluationResults.html) action\.