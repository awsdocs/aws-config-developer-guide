# AWS Config Custom Rules<a name="evaluate-config_develop-rules"></a>

AWS Config Custom Rules are rules that you create from scratch\. There are two ways to create AWS Config custom rules: with Lambda functions \([AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html#gettingstarted-concepts-function)\) and with Guard \([Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard)\), a policy\-as\-code language\.

AWS Config custom rules created with Lambda are called *AWS Config Custom Lambda Rules* and AWS Config custom rules created with Guard are called *AWS Config Custom Policy Rules*\.

## AWS Config Custom Policy Rules<a name="w2aac12c36b7"></a>

Rules written using Guard can be created from the AWS Config console or by using the AWS Config rule APIs\. AWS Config Custom Policy rules allow you to create AWS Config Custom rules without needing to use Java or Python to develop Lambda functions to manage your custom rules\. AWS Config Custom Policy rules are initiated by configuration changes\. For more information about Guard, see the [Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard)\.

## AWS Config Custom Lambda Rules<a name="w2aac12c36b9"></a>

Custom Lambda rules provide you with the option to use Java or Python to create a Lambda function for a AWS Config Custom rule\. A * Lambda function* is custom code that you upload to AWS Lambda, and it is invoked by events that are published to it by an event source\. If the Lambda function is associated with an AWS Config rule, AWS Config invokes it when the rule is initiated\. The Lambda function then evaluates the configuration information that is sent by AWS Config, and it returns the evaluation results\. For more information about Lambda functions, see [Function and Event Sources](https://docs.aws.amazon.com/lambda/latest/dg/intro-core-components.html) in the *AWS Lambda Developer Guide*\.

## Trigger Types<a name="evaluate-config_develop-rules-trigger"></a>

After you add a rule to your account, AWS Config compares your resources to the conditions of the rule\. After this initial evaluation, AWS Config continues to run evaluations each time one is triggered\. The evaluation triggers are defined as part of the rule, and they can include the following types:

**Configuration changes**  
AWS Config runs evaluations for the rule when there is a resource that matches the rule's scope and there is a change in configuration of the resource\. The evaluation runs after AWS Config sends a configuration item change notification\.  
You choose which resources initiate the evaluation by defining the rule's *scope*\. The scope can include the following:  
+ One or more resource types
+ A combination of a resource type and a resource ID
+ A combination of a tag key and value
+ When any recorded resource is created, updated, or deleted
AWS Config runs the evaluation when it detects a change to a resource that matches the rule's scope\. You can use the scope to define which resources initiate evaluations\.

**Periodic**  
AWS Config runs evaluations for the rule at a frequency that you choose; for example, every 24 hours\.

**Hybrid**  
Some rules have both configuration change and periodic triggers\. For these rules, AWS Config evaluates your resources when it detects a configuration change and also at the frequency that you specify\.   


## Evaluation modes<a name="evaluate-config_develop-rules-proactive-detective"></a>

There are two evaluation modes for AWS Config rules:

**Proactive**  
Use proactive evaluation to evaluate resources before they have been deployed\. This allows you to evaluate whether a set of resource properties, if used to define an AWS resource, would be COMPLIANT or NON\_COMPLIANT given the set of proactive rules that you have in your account in your Region\.  
For more information, see and [Evaluation modes](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html#aws-config-rules-evaluation-modes)\. For a list of managed rules that support proactive evaluation, see [List of AWS Config Managed Rules by Evaluation Mode](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-evaluation-mode.html)\.  
Proactive rules do not remediate resources that are flagged as NON\_COMPLIANT or prevent them from being deployed\.

**Detective**  
Use detective evaluation to evaluate resources that have already been deployed\. This allows you to evaluate the configuration settings of your existing resources\.

**Topics**
+ [AWS Config Custom Policy Rules](#w2aac12c36b7)
+ [AWS Config Custom Lambda Rules](#w2aac12c36b9)
+ [Trigger Types](#evaluate-config_develop-rules-trigger)
+ [Evaluation modes](#evaluate-config_develop-rules-proactive-detective)
+ [Creating AWS Config Custom Policy Rules](evaluate-config_develop-rules_cfn-guard.md)
+ [Creating AWS Config Custom Lambda Rules](evaluate-config_develop-rules_lambda-functions.md)