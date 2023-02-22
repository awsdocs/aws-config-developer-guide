# api\-gw\-execution\-logging\-enabled<a name="api-gw-execution-logging-enabled"></a>

Checks that all methods in Amazon API Gateway stage has logging enabled\. The rule is NON\_COMPLIANT if logging is not enabled\. The rule is NON\_COMPLIANT if `loggingLevel` is neither ERROR nor INFO\. 

**Identifier:** API\_GW\_EXECUTION\_LOGGING\_ENABLED

**Resource Types:** AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

loggingLevel \(Optional\)Type: StringDefault: ERROR,INFO  
Comma\-separated list of specific logging levels \(for example, ERROR, INFO or ERROR,INFO\)\.

## AWS CloudFormation template<a name="w2aac12c33c15b9c25c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.