# AWS Config Custom Rules<a name="evaluate-config_develop-rules"></a>

AWS Config Custom Rules are rules that you create from scratch\. There are two ways to create AWS Config custom rules: with Lambda functions \([AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html#gettingstarted-concepts-function)\) and with Guard \([Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard)\), a policy\-as\-code language\.

AWS Config custom rules created with Lambda are called *AWS Config Custom Lambda Rules* and AWS Config custom rules created with Guard are called *AWS Config Custom Policy Rules*\.

## AWS Config Custom Policy Rules<a name="w2aac12c34b7"></a>

Rules written using Guard can be created from the AWS Config console or by using the AWS Config rule APIs\. AWS Config Custom Policy rules allow you to create AWS Config Custom rules without needing to use Java or Python to develop Lambda functions to manage your custom rules\. AWS Config Custom Policy rules are initiated by configuration changes\. For more information about Guard, see the [Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard)\.

## AWS Config Custom Lambda Rules<a name="w2aac12c34b9"></a>

Custom Lambda rules provide you with the option to use Java or Python to create a Lambda function for a AWS Config Custom rule\. A * Lambda function* is custom code that you upload to AWS Lambda, and it is invoked by events that are published to it by an event source\. If the Lambda function is associated with an AWS Config rule, AWS Config invokes it when the rule is initiated\. The Lambda function then evaluates the configuration information that is sent by AWS Config, and it returns the evaluation results\. For more information about Lambda functions, see [Function and Event Sources](https://docs.aws.amazon.com/lambda/latest/dg/intro-core-components.html) in the *AWS Lambda Developer Guide*\.

## Evaluation Mode<a name="w2aac12c34c11"></a>

After you activate a rule, AWS Config compares your resources to the conditions of the rule\. There are two evaluation modes for AWS Config rules: **proactive evaluation** and **detective evaluation**\.

Use *proactive evaluation* to evaluate resources prior to resource provising\. This allows you to evaluate the configuration settings of your resources before they are created or updated\. Use *detective evluation* to evaluate resources that have already been provisioned\. This allows you to evaluate the configuration settings of your existing resources\.

For proactive evaluation, there is only one type of trigger:
+ **Configuration changes** – AWS Config initiates the evaluation when there are changes to the configuration of a pre\-provisioned resource\. The evaluation runs after AWS Config sends a configuration item change notification\.



For detective evaluation, there are two trigger types:
+ **Configuration changes** – AWS Config initiates the evaluation when there are any changes to the configuration of a post\-provisioned resource that matches the rule's scope\. The evaluation runs after AWS Config sends a configuration item change notification\.
+ **Periodic** – AWS Config runs evaluations for the rule at a frequency that you choose \(for example, every 24 hours\)\.

The AWS Config console shows which resources comply with the rule and which rules are being followed\. For more information, see [Viewing Configuration Compliance](evaluate-config_view-compliance.md)\.

**Topics**
+ [AWS Config Custom Policy Rules](#w2aac12c34b7)
+ [AWS Config Custom Lambda Rules](#w2aac12c34b9)
+ [Evaluation Mode](#w2aac12c34c11)
+ [Creating AWS Config Custom Policy Rules](evaluate-config_develop-rules_cfn-guard.md)
+ [Creating AWS Config Custom Lambda Rules](evaluate-config_develop-rules_lambda-functions.md)