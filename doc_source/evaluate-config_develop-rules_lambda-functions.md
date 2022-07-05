# Creating AWS Config Custom Lambda Rules<a name="evaluate-config_develop-rules_lambda-functions"></a>

You can develop custom rules and add them to AWS Config with AWS Lambda functions\. You associate each custom rule with an Lambda function, which contains the logic that evaluates whether your AWS resources comply with the rule\. You associate this function with your rule, and the rule invokes the function either in response to configuration changes or periodically\. The function then evaluates whether your resources comply with your rule, and sends its evaluation results to AWS Config\. 

The example in [Custom Lambda Rules \(Amazon EC2 Example\)](evaluate-config_develop-rules_getting-started.md) guides you through creating a Custom Lambda rule for the first time that evaluates whether each of your EC2 instances is the t2\.micro type\. It includes an example Lambda function that you can add to AWS Lambda with no modification\. The example in [Custom Lambda Rules \(General Example\)](evaluate-config_develop-rules_nodejs.md) provides a more general example for creating Custom Lambda rule\.

To learn how AWS Lambda functions work and how to develop them, see the *[AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/)*\.

**Topics**
+ [Custom Lambda Rules \(Amazon EC2 Example\)](evaluate-config_develop-rules_getting-started.md)
+ [Custom Lambda Rules \(General Example\)](evaluate-config_develop-rules_nodejs.md)
+ [Example AWS Lambda Functions and Events for AWS Config Rules](evaluate-config_develop-rules_examples.md)