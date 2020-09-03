# Example Events for AWS Config Rules<a name="evaluate-config_develop-rules_example-events"></a>

When the trigger for a rule occurs, AWS Config invokes the rule's AWS Lambda function by publishing an event\. Then AWS Lambda executes the function by passing the event to the function's handler\.

## Example Event for Evaluations Triggered by Configuration Changes<a name="triggered-example-event"></a>

AWS Config publishes an event when it detects a configuration change for a resource that is within a rule's scope\. The following example event shows that the rule was triggered by a configuration change for an EC2 instance\.

```
{ 
    "invokingEvent": "{\"configurationItem\":{\"configurationItemCaptureTime\":\"2016-02-17T01:36:34.043Z\",\"awsAccountId\":\"123456789012\",\"configurationItemStatus\":\"OK\",\"resourceId\":\"i-00000000\",\"ARN\":\"arn:aws:ec2:us-east-2:123456789012:instance/i-00000000\",\"awsRegion\":\"us-east-2\",\"availabilityZone\":\"us-east-2a\",\"resourceType\":\"AWS::EC2::Instance\",\"tags\":{\"Foo\":\"Bar\"},\"relationships\":[{\"resourceId\":\"eipalloc-00000000\",\"resourceType\":\"AWS::EC2::EIP\",\"name\":\"Is attached to ElasticIp\"}],\"configuration\":{\"foo\":\"bar\"}},\"messageType\":\"ConfigurationItemChangeNotification\"}",
    "ruleParameters": "{\"myParameterKey\":\"myParameterValue\"}",
    "resultToken": "myResultToken",
    "eventLeftScope": false,
    "executionRoleArn": "arn:aws:iam::123456789012:role/config-role",
    "configRuleArn": "arn:aws:config:us-east-2:123456789012:config-rule/config-rule-0123456",
    "configRuleName": "change-triggered-config-rule",
    "configRuleId": "config-rule-0123456",
    "accountId": "123456789012",
    "version": "1.0"
}
```

## Example Event for Evaluations Triggered by Oversized Configuration Changes<a name="oversized-configuration-item-change-notification-example-event"></a>

Some resource changes generate oversized configuration items\. The following example event shows that the rule was triggered by an oversized configuration change for an EC2 instance\.

```
{
        "invokingEvent": "{\"configurationItemSummary\": {\"changeType\": \"UPDATE\",\"configurationItemVersion\": \"1.2\",\"configurationItemCaptureTime\":\"2016-10-06T16:46:16.261Z\",\"configurationStateId\": 0,\"awsAccountId\":\"123456789012\",\"configurationItemStatus\": \"OK\",\"resourceType\": \"AWS::EC2::Instance\",\"resourceId\":\"i-00000000\",\"resourceName\":null,\"ARN\":\"arn:aws:ec2:us-west-2:123456789012:instance/i-00000000\",\"awsRegion\": \"us-west-2\",\"availabilityZone\":\"us-west-2a\",\"configurationStateMd5Hash\":\"8f1ee69b287895a0f8bc5753eca68e96\",\"resourceCreationTime\":\"2016-10-06T16:46:10.489Z\"},\"messageType\":\"OversizedConfigurationItemChangeNotification\"}",
        "ruleParameters": "{\"myParameterKey\":\"myParameterValue\"}",
        "resultToken": "myResultToken",
        "eventLeftScope": false,
        "executionRoleArn": "arn:aws:iam::123456789012:role/config-role",
        "configRuleArn": "arn:aws:config:us-east-2:123456789012:config-rule/config-rule-ec2-managed-instance-inventory",
        "configRuleName": "change-triggered-config-rule",
        "configRuleId": "config-rule-0123456",
        "accountId": "123456789012",
        "version": "1.0"
    }
```

## Example Event for Evaluations Triggered by Periodic Frequency<a name="periodic-example-event"></a>

AWS Config publishes an event when it evaluates your resources at a frequency that you specify \(such as every 24 hours\)\. The following example event shows that the rule was triggered by a periodic frequency\. 

```
{
    "invokingEvent": "{\"awsAccountId\":\"123456789012\",\"notificationCreationTime\":\"2016-07-13T21:50:00.373Z\",\"messageType\":\"ScheduledNotification\",\"recordVersion\":\"1.0\"}",
    "ruleParameters": "{\"myParameterKey\":\"myParameterValue\"}",
    "resultToken": "myResultToken",
    "eventLeftScope": false,
    "executionRoleArn": "arn:aws:iam::123456789012:role/config-role",
    "configRuleArn": "arn:aws:config:us-east-2:123456789012:config-rule/config-rule-0123456",
    "configRuleName": "periodic-config-rule",
    "configRuleId": "config-rule-6543210",
    "accountId": "123456789012",
    "version": "1.0"
}
```

## Event Attributes<a name="w22aac11c31c25c11c11"></a>

The JSON object for an AWS Config event contains the following attributes:

`invokingEvent`  
The event that triggers the evaluation for a rule\. If the event is published in response to a resource configuration change, the value for this attribute is a string that contains a JSON `configurationItem` or a `configurationItemSummary` \(for oversized configuration items\)\. The configuration item represents the state of the resource at the moment that AWS Config detected the change\. For an example of a configuration item, see the output produced by the `get-resource-config-history` AWS CLI command in [Viewing Configuration History](view-manage-resource-console.md#get-config-history-cli)\.  
If the event is published for a periodic evaluation, the value is a string that contains a JSON object\. The object includes information about the evaluation that was triggered\.  
For each type of event, a function must parse the string with a JSON parser to be able to evaluate its contents, as shown in the following Node\.js example:  

```
var invokingEvent = JSON.parse(event.invokingEvent);
```

`ruleParameters`  
Key/value pairs that the function processes as part of its evaluation logic\. You define parameters when you use the AWS Config console to create a custom rule\. You can also define parameters with the `InputParameters` attribute in the `PutConfigRule` AWS Config API request or the `put-config-rule` AWS CLI command\.  
The JSON code for the parameters is contained within a string, so a function must parse the string with a JSON parser to be able to evaluate its contents, as shown in the following Node\.js example:  

```
var ruleParameters = JSON.parse(event.ruleParameters);
```

`resultToken`  
A token that the function must pass to AWS Config with the `PutEvaluations` call\.

`eventLeftScope`  
A Boolean value that indicates whether the AWS resource to be evaluated has been removed from the rule's scope\. If the value is `true`, the function indicates that the evaluation can be ignored by passing `NOT_APPLICABLE` as the value for the `ComplianceType` attribute in the `PutEvaluations` call\.

`executionRoleArn`  
The ARN of the IAM role that is assigned to AWS Config\.

`configRuleArn`  
The ARN that AWS Config assigned to the rule\.

`configRuleName`  
The name that you assigned to the rule that caused AWS Config to publish the event and invoke the function\.

`configRuleId`  
The ID that AWS Config assigned to the rule\.

`accountId`  
The ID of the AWS account that owns the rule\.

`version`  
A version number assigned by AWS\. The version will increment if AWS adds attributes to AWS Config events\. If a function requires an attribute that is only in events that match or exceed a specific version, then that function can check the value of this attribute\.  
The current version for AWS Config events is 1\.0\.