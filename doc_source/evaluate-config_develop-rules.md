# AWS Config Custom Rules<a name="evaluate-config_develop-rules"></a>

You can develop custom rules and add them to AWS Config\. You associate each custom rule with an AWS Lambda function, which contains the logic that evaluates whether your AWS resources comply with the rule\.

You associate this function with your rule, and the rule invokes the function either in response to configuration changes or periodically\. The function then evaluates whether your resources comply with your rule, and sends its evaluation results to AWS Config\. 

The exercise in [Getting Started with Custom Rules for AWS Config](evaluate-config_develop-rules_getting-started.md) guides you through creating a custom rule for the first time\. It includes an example function that you can add to AWS Lambda with no modification\.

To learn how AWS Lambda functions work and how to develop them, see the *[AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/)*\.

**Topics**
+ [Getting Started with Custom Rules for AWS Config](evaluate-config_develop-rules_getting-started.md)
+ [Developing a Custom Rule for AWS Config](evaluate-config_develop-rules_nodejs.md)
+ [Example AWS Lambda Functions and Events for AWS Config Rules](evaluate-config_develop-rules_examples.md)