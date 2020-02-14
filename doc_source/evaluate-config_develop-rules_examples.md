# Example AWS Lambda Functions and Events for AWS Config Rules<a name="evaluate-config_develop-rules_examples"></a>

Each custom Config rule is associated with an AWS Lambda *function*, which is custom code that contains the evaluation logic for the rule\. When the trigger for a Config rule occurs \(for example, when AWS Config detects a configuration change\), AWS Config invokes the rule's Lambda function by publishing an *event*, which is a JSON object that provides the configuration data that the function evaluates\.

For more information about functions and events in AWS Lambda, see [Function and Event Sources](https://docs.aws.amazon.com/lambda/latest/dg/intro-core-components.html) in the *AWS Lambda Developer Guide*\.

**Topics**
+ [Example AWS Lambda Functions for AWS Config Rules \(Node\.js\)](evaluate-config_develop-rules_nodejs-sample.md)
+ [Example Events for AWS Config Rules](evaluate-config_develop-rules_example-events.md)