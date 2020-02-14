# Working with AWS Config Managed Rules<a name="managing-aws-managed-rules"></a>

You can set up and activate AWS managed rules from the AWS Management Console, AWS CLI, or AWS Config API\.

## Setting Up and Activating an AWS Managed Rule \(Console\)<a name="setup-activate-managed-rule-console"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the region selector is set to a region that supports AWS Config rules\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\.

1. In the left navigation, choose **Rules**\.

1. On the **Rules** page, choose **Add rule**\.

1. On the **Rules** page, you can do the following:
   + Type in the search field to filter results by rule name, description, and label\. For example, type **EC2** to return rules that evaluate EC2 resource types or type **periodic** to return rules that are triggered periodically\.
   + Choose the arrow icon to see the next page of rules\. Recently added rules are marked as **New**\. 

1. Choose a rule that you want to create\.

1. On the **Configure rule** page, configure the rule by completing the following steps:

   1. For **Name**, type a unique name for the rule\.

   1. If the trigger types for your rule include **Configuration changes**, specify one of the following options for **Scope of changes** with which AWS Config invokes your Lambda function:
      + **Resources** – When a resource that matches the specified resource type, or the type plus identifier, is created, changed, or deleted\.
      + **Tags** – When a resource with the specified tag is created, changed, or deleted\.
      + **All changes** – When a resource recorded by AWS Config is created, changed, or deleted\.

   1. If the trigger types for your rule include **Periodic**, specify the **Frequency** with which AWS Config invokes your Lambda function\.

   1. If your rule includes parameters in the **Rule parameters** section, you can customize the values for the provided keys\. A parameter is an attribute that your resources must have before they are considered COMPLIANT with the rule\.

1. Choose **Save**\. Your new rule displays on the **Rules** page\.

   **Compliance** will display **Evaluating\.\.\.** until AWS Config has evaluation results for your rule\. A summary of the results appears after several minutes\. You can update the results with the refresh button\.

   If the rule or function is not working as expected, you might see one of the following for **Compliance**:
   + **No results reported** \- AWS Config evaluated your resources against the rule\. The rule did not apply to the AWS resources in its scope, the specified resources were deleted, or the evaluation results were deleted\. To get evaluation results, update the rule, change its scope, or choose **Re\-evaluate**\. 

     This message may also appear if the rule didn't report evaluation results\.
   + **No resources in scope ** \- AWS Config cannot evaluate your recorded AWS resources against this rule because none of your resources are within the rule’s scope\. To get evaluation results, edit the rule and change its scope, or add resources for AWS Config to record by using the **Settings** page\.
   + **Evaluations failed** \- For information that can help you determine the problem, choose the rule name to open its details page and see the error message\.

## Activating an AWS Managed Rule \(AWS CLI\)<a name="setup-activate-managed-rule-cli"></a>

Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-config-rule.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-config-rule.html) command\.

## Activating an AWS Managed Rule \(API\)<a name="setup-activate-managed-rule-api"></a>

Use the [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html) action\.