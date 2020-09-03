# Developing a Custom Rule for AWS Config<a name="evaluate-config_develop-rules_nodejs"></a>

Complete the following procedure to create a custom rule\. To create a custom rule, you first create an AWS Lambda function, which contains the evaluation logic for the rule\. Then you associate the function with a custom rule that you create in AWS Config\.

**Contents**
+ [Creating an AWS Lambda Function for a Custom Config Rule](#create-lambda-function-for-custom-config-rule)
+ [Creating a Custom Rule in AWS Config](#creating-a-custom-rule-with-the-AWS-Config-console)
+ [Evaluating Additional Resource Types](#creating-custom-rules-for-additional-resource-types)

## Creating an AWS Lambda Function for a Custom Config Rule<a name="create-lambda-function-for-custom-config-rule"></a>

A *Lambda function* is custom code that you upload to AWS Lambda, and it is invoked by events that are published to it by an event source\. If the Lambda function is associated with a Config rule, AWS Config invokes it when the rule's trigger occurs\. The Lambda function then evaluates the configuration information that is sent by AWS Config, and it returns the evaluation results\. For more information about Lambda functions, see [Function and Event Sources](https://docs.aws.amazon.com/lambda/latest/dg/intro-core-components.html) in the *AWS Lambda Developer Guide*\.

You can use a programming language that is supported by AWS Lambda to create a Lambda function for a custom rule\. To make this task easier, you can customize an AWS Lambda blueprint or reuse a sample function from the AWS Config Rules GitHub repository\.

****AWS Lambda** blueprints**  
The AWS Lambda console provides sample functions, or *blueprints*, which you can customize by adding your own evaluation logic\. When you create a function, you can choose one of the following blueprints:
+ **config\-rule\-change\-triggered** – Triggered when your AWS resource configurations change\.
+ **config\-rule\-periodic** – Triggered at a frequency that you choose \(for example, every 24 hours\)\.

**AWS Config Rules GitHub repository**  
A public repository of sample functions for custom rules is available on GitHub, a web\-based code hosting and sharing service\. The sample functions are developed and contributed by the AWS community\. If you want to use a sample, you can copy its code into a new AWS Lambda function\. To view the repository, see [https://github.com/awslabs/aws-config-rules/](https://github.com/awslabs/aws-config-rules/)\.

**To create the function for your custom rule**

1. Sign in to the AWS Management Console and open the AWS Lambda console at [https://console\.aws\.amazon\.com/lambda/](https://console.aws.amazon.com/lambda/)\.

1. In the AWS Management Console menu, verify that the region selector is set to a region that supports AWS Config rules\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\.

1. Choose **Create a Lambda function**\.

1. On the **Select blueprint** page, you can choose one of the blueprint functions for AWS Config rules as a starting point, or you can proceed without a blueprint by choosing **Skip**\.

1. On the **Configure triggers** page, choose **Next**\.

1. On the **Configure function** page, type a name and description\.

1. For **Runtime**, choose the programming language in which your function is written\.

1. For **Code entry type**, choose your preferred entry type\. If you are using a blueprint, keep **Edit code inline**\.

1. Provide your code using the method required by the code entry type that you selected\. If you are using a blueprint, the function code is provided in the code editor, and you can customize it to include your own evaluation logic\. Your code can evaluate the event data that AWS Config provides when it invokes your function:
   + For functions based on the **config\-rule\-change\-triggered** blueprint, or for functions triggered by configuration changes, the event data is the configuration item or an oversized configuration item object for the AWS resource that changed\.
   + For functions based on the **config\-rule\-periodic** blueprint, or for functions triggered at a frequency that you choose, the event data is a JSON object that includes information about when the evaluation was triggered\.
   + For both types of functions, AWS Config passes rule parameters in JSON format\. You can define which rule parameters are passed when you create the custom rule in AWS Config\.
   + For example events that AWS Config publishes when it invokes your function, see [Example Events for AWS Config Rules](evaluate-config_develop-rules_example-events.md)\.

1. For **Handler**, specify the handler for your function\. If you are using a blueprint, keep the default value\.

1. For **Role**, choose **Create new role from template\(s\)**\.

1. For **Role name**, type a name\.

1. For **Policy templates**, choose **AWS Config Rules permission**\. 

1. On the **Configure function** page, choose **Next**\.

1. On the **Review page**, verify the details about your function, and choose **Create function**\.

## Creating a Custom Rule in AWS Config<a name="creating-a-custom-rule-with-the-AWS-Config-console"></a>

Use AWS Config to create a custom rule and associate the rule with a Lambda function\.

**To create a custom rule**

1. Open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the region selector is set to the same region in which you created the AWS Lambda function for your custom rule\.

1. On the **Rules** page, choose **Add rule**\.

1. On the **Add rule** page, choose **Add custom rule**\.

1. On the **Configure rule** page, type a name and description\.

1. For **AWS Lambda function ARN**, specify the ARN that AWS Lambda assigned to your function\.
**Note**  
The ARN that you specify in this step must not include the `$LATEST` qualifier\. You can specify an ARN without a version qualifier or with any qualifier besides `$LATEST`\. AWS Lambda supports function versioning, and each version is assigned an ARN with a qualifier\. AWS Lambda uses the `$LATEST` qualifier for the latest version\.

1. For **Trigger type**, choose one or both of the following:
   + **Configuration changes** – AWS Config invokes your Lambda function when it detects a configuration change\.
   + **Periodic** – AWS Config invokes your Lambda function at the frequency that you choose \(for example, every 24 hours\)\. 

1. If the trigger types for your rule include **Configuration changes**, specify one of the following options for **Scope of changes** with which AWS Config invokes your Lambda function:
   + **Resources** – When a resource that matches the specified resource type, or the type plus identifier, is created, changed, or deleted\.
   + **Tags** – When a resource with the specified tag is created, changed, or deleted\.
   + **All changes** – When a resource recorded by AWS Config is created, changed, or deleted\.

1. If the trigger types for your rule include **Periodic**, specify the **Frequency** with which AWS Config invokes your Lambda function\.

1. In the **Rule parameters** section, specify any rule parameters that your AWS Lambda function evaluates and the desired value\.

1. Choose **Save**\. Your new rule displays on the **Rules** page\.

   **Compliance** will display **Evaluating\.\.\.** until AWS Config receives evaluation results from your AWS Lambda function\. If the rule and the function are working as expected, a summary of results appears after several minutes\. You can update the results with the refresh button\.

   If the rule or function is not working as expected, you might see one of the following for **Compliance**:
   + **No results reported** \- AWS Config evaluated your resources against the rule\. The rule did not apply to the AWS resources in its scope, the specified resources were deleted, or the evaluation results were deleted\. To get evaluation results, update the rule, change its scope, or choose **Re\-evaluate**\.

     This message may also appear if the rule didn't report evaluation results\.
   + **No resources in scope ** \- AWS Config cannot evaluate your recorded AWS resources against this rule because none of your resources are within the rule’s scope\. You can choose which resources AWS Config records on the **Settings** page\.
   + **Evaluations failed** \- For information that can help you determine the problem, choose the rule name to open its details page and see the error message\.

**Note**  
When you create a custom rule with the AWS Config console, the appropriate permissions are automatically created for you\. If you create a custom rule with the AWS CLI, you need to give AWS Config permission to invoke your Lambda function, using the `aws lambda add-permission` command\. For more information, see [Using Resource\-Based Policies for AWS Lambda \(Lambda Function Policies\)](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) in the *AWS Lambda Developer Guide*\.

## Evaluating Additional Resource Types<a name="creating-custom-rules-for-additional-resource-types"></a>

You can create custom rules to run evaluations for resource types not yet recorded by AWS Config\. This is useful if you want to evaluate compliance for additional resource types that AWS Config doesn't currently record\. For a list of additional resource types that you can evaluate with custom rules, see [AWS Resource Types Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)\.

**Note**  
The list in the AWS CloudFormation User Guide may contain recently added resource types that are not yet available for creating custom rules in AWS Config\. AWS Config adds resource types support at regular intervals\.

**Example**

1. You want to evaluate Amazon S3 Glacier vaults in your account\. Amazon S3 Glacier vault resources are currently not recorded by AWS Config\.

1. You create an AWS Lambda function that evaluates whether your Amazon S3 Glacier vaults comply with your account requirements\.

1. You create a custom rule named **evaluate\-glacier\-vaults ** and then assign your AWS Lambda function to the rule\.

1. AWS Config invokes your Lambda function and then evaluates the Amazon S3 Glacier vaults against your rule\.

1. AWS Config returns the evaluations and you can view the compliance results for your rule\.

**Note**  
You can view the configuration details in the AWS Config timeline and look up resources in the AWS Config console for resources that AWS Config supports\. If you configured AWS Config to record all resource types, newly supported resources will automatically be recorded\. For more information, see [Supported Resource Types](resource-config-reference.md)\.