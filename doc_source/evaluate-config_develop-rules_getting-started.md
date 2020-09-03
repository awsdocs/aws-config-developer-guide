# Getting Started with Custom Rules for AWS Config<a name="evaluate-config_develop-rules_getting-started"></a>

This procedure guides you through the process of creating a custom rule that evaluates whether each of your EC2 instances is the t2\.micro type\. AWS Config will run event\-based evaluations for this rule, meaning it will check your instance configurations each time AWS Config detects a configuration change in an instance\. AWS Config will flag t2\.micro instances as compliant and all other instances as noncompliant\. The compliance status will appear in the AWS Config console\.

To have the best outcome with this procedure, you should have one or more EC2 instances in your AWS account\. Your instances should include a combination of at least one t2\.micro instance and other types\.

To create this rule, first, you will create an AWS Lambda function by customizing a blueprint in the AWS Lambda console\. Then, you will create a custom rule in AWS Config, and you will associate the rule with the function\.

**Topics**
+ [Creating an AWS Lambda Function for a Custom Config Rule](#gs-create-lambda-function-for-custom-config-rule)
+ [Creating a Custom Rule](#gs-creating-a-custom-rule-with-the-AWS-Config-console)

## Creating an AWS Lambda Function for a Custom Config Rule<a name="gs-create-lambda-function-for-custom-config-rule"></a>

1. Sign in to the AWS Management Console and open the AWS Lambda console at [https://console\.aws\.amazon\.com/lambda/](https://console.aws.amazon.com/lambda/)\.

1. In the AWS Management Console menu, verify that the region selector is set to a region that supports AWS Config rules\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\.

1. In the AWS Lambda console, choose **Create a Lambda function**\.

1. On the **Select blueprint** page, for **filter**, type **config\-rule\-change\-triggered**\. Select the blueprint in the filter results\. 

1. On the **Configure triggers** page, choose **Next**\.

1. On the **Configure function** page, complete the following steps:

   1. For **Name**, type **InstanceTypeCheck**\.

   1. For **Runtime**, keep **Node\.js**\.

   1. For **Code entry type**, keep **Edit code inline**\. The Node\.js code for your function is provided in the code editor\. For this procedure, you do not need to change the code\.

   1. For **Handler**, keep **index\.handler**\.

   1. For **Role**, choose **Create new role from template\(s\)**\.

   1. For **Role name**, type a name\.

   1. For **Policy templates**, choose **AWS Config Rules permission**\. 

   1. On the **Configure function** page, choose **Next**\.

   1. On the **Review page**, verify the details about your function, and choose **Create function**\. The AWS Lambda console displays your function\.

1. To verify that your function is set up correctly, test it with the following steps:

   1. Choose **Actions**, and then choose **Configure test event**\.

   1. In the **Input test event** window, for **Sample event template**, choose **AWS Config Change Triggered Rule**\.

   1. Choose **Save and test**\. AWS Lambda tests your function with the example event\. If your function is working as expected, an error message similar to the following appears under **Execution result**:

      ```
      {
        "errorMessage": "Result Token provided is invalid",
        "errorType": "InvalidResultTokenException",
      . . .
      ```

      The `InvalidResultTokenException` is expected because your function runs successfully only when it receives a *result token* from AWS Config\. The result token identifies the AWS Config rule and the event that caused the evaluation, and the result token associates an evaluation with a rule\. This exception indicates that your function has the permission it needs to send results to AWS Config\. Otherwise, the following error message appears: `not authorized to perform: config:PutEvaluations`\. If this error occurs, update the role that you assigned to your function to allow the `config:PutEvaluations` action, and test your function again\.

## Creating a Custom Rule<a name="gs-creating-a-custom-rule-with-the-AWS-Config-console"></a>

1. Open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the region selector is set to the same region in which you created the AWS Lambda function for your custom rule\.

1. On the **Rules** page, choose **Add rule**\.

1. On the **Add rule** page, choose **Add custom rule**\.

1. On the **Configure rule** page, complete the following steps:

   1. For **Name**, type **InstanceTypesAreT2micro**\.

   1. For **Description**, type **Evaluates whether EC2 instances are the t2\.micro type**\.

   1. For **AWS Lambda function ARN**, specify the ARN that AWS Lambda assigned to your function\.
**Note**  
The ARN that you specify in this step must not include the `$LATEST` qualifier\. You can specify an ARN without a version qualifier or with any qualifier besides `$LATEST`\. AWS Lambda supports function versioning, and each version is assigned an ARN with a qualifier\. AWS Lambda uses the `$LATEST` qualifier for the latest version\. 

   1. For **Trigger type**, choose **Configuration changes**\.

   1. For **Scope of changes**, choose **Resources**\.

   1. For **Resources**, choose **Instance**\.

   1. In the **Rule parameters** section, you must specify the rule parameter that your AWS Lambda function evaluates and the desired value\. The function for this procedure evaluates the `desiredInstanceType` parameter\.

      For **Key**, type **desiredInstanceType**\. For **Value**, type **t2\.micro**\.

1. Choose **Save**\. Your new rule displays on the **Rules** page\. 

   **Compliance** will display **Evaluating\.\.\.** until AWS Config receives evaluation results from your AWS Lambda function\. If the rule and the function are working as expected, a summary of the results appears after several minutes\. For example, a result of **2 noncompliant resource\(s\)** indicates that 2 of your instances are not t2\.micro instances, and a result of **Compliant** indicates that all instances are t2\.micro\. You can update the results with the refresh button\.

   If the rule or function is not working as expected, you might see one of the following for **Compliance**:
   + **No results reported** \- AWS Config evaluated your resources against the rule\. The rule did not apply to the AWS resources in its scope, the specified resources were deleted, or the evaluation results were deleted\. To get evaluation results, update the rule, change its scope, or choose **Re\-evaluate**\. 

     Verify that the scope includes **Instance** for **Resources**, and try again\.
   + **No resources in scope ** \- AWS Config cannot evaluate your recorded AWS resources against this rule because none of your resources are within the rule’s scope\. To get evaluation results, edit the rule and change its scope, or add resources for AWS Config to record by using the **Settings** page\.

     Verify that AWS Config is recording EC2 instances\.
   + **Evaluations failed** \- For information that can help you determine the problem, choose the rule name to open its details page and see the error message\.

If your rule works correctly and AWS Config provides evaluation results, you can learn which conditions affect the compliance status of your rule\. You can learn which resources, if any, are noncompliant, and why\. For more information, see [Viewing Configuration Compliance](evaluate-config_view-compliance.md)\.