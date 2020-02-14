# Example AWS Lambda Functions for AWS Config Rules \(Node\.js\)<a name="evaluate-config_develop-rules_nodejs-sample"></a>

AWS Lambda executes functions in response to events that are published by AWS services\. The function for a custom Config rule receives an event that is published by AWS Config, and the function then uses data that it receives from the event and that it retrieves from the AWS Config API to evaluate the compliance of the rule\. The operations in a function for a Config rule differ depending on whether it performs an evaluation that is triggered by configuration changes or triggered periodically\.

For information about common patterns within AWS Lambda functions, see [Programming Model](https://docs.aws.amazon.com/lambda/latest/dg/programming-model-v2.html) in the *AWS Lambda Developer Guide*\.

**Contents**
+ [Example Function for Evaluations Triggered by Configuration Changes](#event-based-example-rule)
+ [Example Function for Periodic Evaluations](#periodic-example-rule)

## Example Function for Evaluations Triggered by Configuration Changes<a name="event-based-example-rule"></a>

AWS Config will invoke a function like the following example when it detects a configuration change for a resource that is within a custom rule's scope\.

If you use the AWS Config console to create a rule that is associated with a function like this example, choose **Configuration changes** as the trigger type\. If you use the AWS Config API or AWS CLI to create the rule, set the `MessageType` attribute to `ConfigurationItemChangeNotification` and `OversizedConfigurationItemChangeNotification`\. These settings enable your rule to be triggered whenever AWS Config generates a configuration item or an oversized configuration item as a result of a resource change\.

This example evaluates your resources and checks whether the instances match the resource type, `AWS::EC2::Instance`\. The rule is triggered when AWS Config generates a configuration item or an oversized configuration item notification\. 

```
'use strict';

const aws = require('aws-sdk');

const config = new aws.ConfigService();


// Helper function used to validate input
function checkDefined(reference, referenceName) {
    if (!reference) {
        throw new Error(`Error: ${referenceName} is not defined`);
    }
    return reference;
}

// Check whether the message type is OversizedConfigurationItemChangeNotification,
function isOverSizedChangeNotification(messageType) {
    checkDefined(messageType, 'messageType');
    return messageType === 'OversizedConfigurationItemChangeNotification';
}

// Get the configurationItem for the resource using the getResourceConfigHistory API.
function getConfiguration(resourceType, resourceId, configurationCaptureTime, callback) {
    config.getResourceConfigHistory({ resourceType, resourceId, laterTime: new Date(configurationCaptureTime), limit: 1 }, (err, data) => {
        if (err) {
            callback(err, null);
        }
        const configurationItem = data.configurationItems[0];
        callback(null, configurationItem);
    });
}

// Convert the oversized configuration item from the API model to the original invocation model.
function convertApiConfiguration(apiConfiguration) {
    apiConfiguration.awsAccountId = apiConfiguration.accountId;
    apiConfiguration.ARN = apiConfiguration.arn;
    apiConfiguration.configurationStateMd5Hash = apiConfiguration.configurationItemMD5Hash;
    apiConfiguration.configurationItemVersion = apiConfiguration.version;
    apiConfiguration.configuration = JSON.parse(apiConfiguration.configuration);
    if ({}.hasOwnProperty.call(apiConfiguration, 'relationships')) {
        for (let i = 0; i < apiConfiguration.relationships.length; i++) {
            apiConfiguration.relationships[i].name = apiConfiguration.relationships[i].relationshipName;
        }
    }
    return apiConfiguration;
}

// Based on the message type, get the configuration item either from the configurationItem object in the invoking event or with the getResourceConfigHistory API in the getConfiguration function.
function getConfigurationItem(invokingEvent, callback) {
    checkDefined(invokingEvent, 'invokingEvent');
    if (isOverSizedChangeNotification(invokingEvent.messageType)) {
       const configurationItemSummary = checkDefined(invokingEvent.configurationItemSummary, 'configurationItemSummary');
        getConfiguration(configurationItemSummary.resourceType, configurationItemSummary.resourceId, configurationItemSummary.configurationItemCaptureTime, (err, apiConfigurationItem) => {
            if (err) {
                callback(err);
            }
            const configurationItem = convertApiConfiguration(apiConfigurationItem);
            callback(null, configurationItem);
       });
    } else {
        checkDefined(invokingEvent.configurationItem, 'configurationItem');
        callback(null, invokingEvent.configurationItem);
    }
}

// Check whether the resource has been deleted. If the resource was deleted, then the evaluation returns not applicable.
function isApplicable(configurationItem, event) {
    checkDefined(configurationItem, 'configurationItem');
    checkDefined(event, 'event');
    const status = configurationItem.configurationItemStatus;
    const eventLeftScope = event.eventLeftScope;
    return (status === 'OK' || status === 'ResourceDiscovered') && eventLeftScope === false;
}

// In this example, the resource is compliant if it is an instance and its type matches the type specified as the desired type.
// If the resource is not an instance, then this resource is not applicable.
function evaluateChangeNotificationCompliance(configurationItem, ruleParameters) {
    checkDefined(configurationItem, 'configurationItem');
    checkDefined(configurationItem.configuration, 'configurationItem.configuration');
    checkDefined(ruleParameters, 'ruleParameters');

    if (configurationItem.resourceType !== 'AWS::EC2::Instance') {
        return 'NOT_APPLICABLE';
    } else if (ruleParameters.desiredInstanceType === configurationItem.configuration.instanceType) {
        return 'COMPLIANT';
    }
    return 'NON_COMPLIANT';
}

// Receives the event and context from AWS Lambda.
exports.handler = (event, context, callback) => {
    checkDefined(event, 'event');
    const invokingEvent = JSON.parse(event.invokingEvent);
    const ruleParameters = JSON.parse(event.ruleParameters);
    getConfigurationItem(invokingEvent, (err, configurationItem) => {
        if (err) {
            callback(err);
        }
        let compliance = 'NOT_APPLICABLE';
        const putEvaluationsRequest = {};
        if (isApplicable(configurationItem, event)) {
            // Invoke the compliance checking function.
            compliance = evaluateChangeNotificationCompliance(configurationItem, ruleParameters);
        }
        // Initializes the request that contains the evaluation results.
        putEvaluationsRequest.Evaluations = [
            {
                ComplianceResourceType: configurationItem.resourceType,
                ComplianceResourceId: configurationItem.resourceId,
                ComplianceType: compliance,
                OrderingTimestamp: configurationItem.configurationItemCaptureTime,
            },
        ];
        putEvaluationsRequest.ResultToken = event.resultToken;

        // Sends the evaluation results to AWS Config.
        config.putEvaluations(putEvaluationsRequest, (error, data) => {
            if (error) {
                callback(error, null);
            } else if (data.FailedEvaluations.length > 0) {
                // Ends the function if evaluation results are not successfully reported to AWS Config.
                callback(JSON.stringify(data), null);
            } else {
                callback(null, data);
            }
        });
    });
};
```

**Function Operations**

The function performs the following operations at runtime:

1. The function runs when AWS Lambda passes the `event` object to the `handler` function\. AWS Lambda also passes a `context` object, which contains information and methods that the function can use while it runs\. In this example, the function accepts the optional `callback` parameter, which it uses to return information to the caller\.

1. The function checks whether the `messageType` for the event is a configuration item or an oversized configuration item, and then returns the configuration item\. 

1. The handler calls the `isApplicable` function to determine whether the resource was deleted\.

1. The handler calls the `evaluateChangeNotificationCompliance` function and passes the `configurationItem` and `ruleParameters` objects that AWS Config published in the event\.

   The function first evaluates whether the resource is an EC2 instance\. If the resource is not an EC2 instance, the function returns a compliance value of `NOT_APPLICABLE`\. 

   The function then evaluates whether the `instanceType` attribute in the configuration item is equal to the `desiredInstanceType` parameter value\. If the values are equal, the function returns `COMPLIANT`\. If the values are not equal, the function returns `NON_COMPLIANT`\.

1. The handler prepares to send the evaluation results to AWS Config by initializing the `putEvaluationsRequest` object\. This object includes the `Evaluations` parameter, which identifies the compliance result, the resource type, and the ID of the resource that was evaluated\. The `putEvaluationsRequest` object also includes the result token from the event, which identifies the rule and the event for AWS Config\. 

1. The handler sends the evaluation results to AWS Config by passing the object to the `putEvaluations` method of the `config` client\.

## Example Function for Periodic Evaluations<a name="periodic-example-rule"></a>

AWS Config will invoke a function like the following example for periodic evaluations\. Periodic evaluations occur at the frequency that you specify when you define the rule in AWS Config\.

If you use the AWS Config console to create a rule that is associated with a function like this example, choose **Periodic** as the trigger type\. If you use the AWS Config API or AWS CLI to create the rule, set the `MessageType` attribute to `ScheduledNotification`\.

This example checks whether the total number of a specified resource exceeds a specified maximum\.

```
var aws = require('aws-sdk'), // Loads the AWS SDK for JavaScript.
    config = new aws.ConfigService(), // Constructs a service object to use the aws.ConfigService class.
    COMPLIANCE_STATES = {
        COMPLIANT : 'COMPLIANT',
        NON_COMPLIANT : 'NON_COMPLIANT',
        NOT_APPLICABLE : 'NOT_APPLICABLE'
    };

// Receives the event and context from AWS Lambda.
exports.handler = function(event, context, callback) {
    // Parses the invokingEvent and ruleParameters values, which contain JSON objects passed as strings.
    var invokingEvent = JSON.parse(event.invokingEvent), 
        ruleParameters = JSON.parse(event.ruleParameters),
        noOfResources = 0;

    if (isScheduledNotification(invokingEvent)) {
        countResourceTypes(ruleParameters.applicableResourceType, "", noOfResources, function(err, count) {
            if (err === null) {
                var putEvaluationsRequest;
                // Initializes the request that contains the evaluation results.
                putEvaluationsRequest = {
                    Evaluations : [ {
                        // Applies the evaluation result to the AWS account published in the event.
                        ComplianceResourceType : 'AWS::::Account',
                        ComplianceResourceId : event.accountId,
                        ComplianceType : evaluateCompliance(ruleParameters.maxCount, count),
                        OrderingTimestamp : new Date()
                    } ],
                    ResultToken : event.resultToken
                };
                // Sends the evaluation results to AWS Config.
                config.putEvaluations(putEvaluationsRequest, function(err, data) {
                    if (err) {
                        callback(err, null);
                    } else {
                        if (data.FailedEvaluations.length > 0) {
                            // Ends the function execution if evaluation results are not successfully reported
                            callback(JSON.stringify(data));
                        }
                        callback(null, data);
                    }
                });
            } else {
                callback(err, null);
            }
        });
    } else {
        console.log("Invoked for a notification other than Scheduled Notification... Ignoring.");
    }
};

// Checks whether the invoking event is ScheduledNotification.
function isScheduledNotification(invokingEvent) {
    return (invokingEvent.messageType === 'ScheduledNotification');
}

// Checks whether the compliance conditions for the rule are violated.
function evaluateCompliance(maxCount, actualCount) {
    if (actualCount > maxCount) {
        return COMPLIANCE_STATES.NON_COMPLIANT;
    } else {
        return COMPLIANCE_STATES.COMPLIANT;
    }
}

// Counts the applicable resources that belong to the AWS account.
function countResourceTypes(applicableResourceType, nextToken, count, callback) {
    config.listDiscoveredResources({resourceType : applicableResourceType, nextToken : nextToken}, function(err, data) {
        if (err) {
            callback(err, null);
        } else {
            count = count + data.resourceIdentifiers.length;
            if (data.nextToken !== undefined && data.nextToken != null) {
                countResourceTypes(applicableResourceType, data.nextToken, count, callback);
            }
            callback(null, count);
        }
    });
    return count;
}
```

**Function Operations**

The function performs the following operations at runtime:

1. The function runs when AWS Lambda passes the `event` object to the `handler` function\. AWS Lambda also passes a `context` object, which contains information and methods that the function can use while it runs\. In this example, the function accepts the optional `callback` parameter, which it uses to return information to the caller\.

1. To count the resources of the specified type, the handler calls the `countResourceTypes` function, and it passes the `applicableResourceType` parameter that it received from the event\. The `countResourceTypes` function calls the `listDiscoveredResources` method of the `config` client, which returns a list of identifiers for the applicable resources\. The function uses the length of this list to determine the number of applicable resources, and it returns this count to the handler\.

1. The handler prepares to send the evaluation results to AWS Config by initializing the `putEvaluationsRequest` object\. This object includes the `Evaluations` parameter, which identifies the compliance result and the AWS account that was published in the event\. You can use the `Evaluations` parameter to apply the result to any resource type that is supported by AWS Config\. The `putEvaluationsRequest` object also includes the result token from the event, which identifies the rule and the event for AWS Config\.

1. Within the `putEvaluationsRequest` object, the handler calls the `evaluateCompliance` function\. This function tests whether the number of applicable resources exceeds the maximum assigned to the `maxCount` parameter, which was provided by the event\. If the number of resources exceeds the maximum, the function returns `NON_COMPLIANT`\. If the number of resources does not exceed the maximum, the function returns `COMPLIANT`\.

1. The handler sends the evaluation results to AWS Config by passing the object to the `putEvaluations` method of the `config` client\.