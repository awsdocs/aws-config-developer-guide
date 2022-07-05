# AWS Config Custom Rules<a name="evaluate-config_develop-rules"></a>

You can use Guard Custom policy or Lambda functions to develop Custom Policy Rules or Custom Lambda Rules and add them to AWS Config\.

Guard is a policy\-as\-code language that allows you to write policies that are enforced by AWS Config Custom Policy rules\. Rules written using Guard can be created from the AWS Config console or by using the AWS Config rule APIs\. AWS Config Custom Policy rules allow you to create AWS Config Custom rules without needing to use Java or Python to develop Lambda functions to manage your custom rules\. AWS Config Custom Policy rules are initiated by configuration changes\. For more information about Guard, see the [Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard)\.

Custom Lambda rules provide you with the option to use Java or Python to create a Lambda function for a AWS Config Custom rule\. A * Lambda function* is custom code that you upload to AWS Lambda, and it is invoked by events that are published to it by an event source\. If the Lambda function is associated with an AWS Config rule, AWS Config invokes it when the rule is initiated\. The Lambda function then evaluates the configuration information that is sent by AWS Config, and it returns the evaluation results\. For more information about Lambda functions, see [Function and Event Sources](https://docs.aws.amazon.com/lambda/latest/dg/intro-core-components.html) in the *AWS Lambda Developer Guide*\.

**Topics**
+ [Creating AWS Config Custom Policy Rules](evaluate-config_develop-rules_cfn-guard.md)
+ [Creating AWS Config Custom Lambda Rules](evaluate-config_develop-rules_lambda-functions.md)