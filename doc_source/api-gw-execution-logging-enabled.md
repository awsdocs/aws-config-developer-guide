# api\-gw\-execution\-logging\-enabled<a name="api-gw-execution-logging-enabled"></a>

Checks that all methods in Amazon API Gateway stage has logging enabled\. The rule is NON\_COMPLIANT if logging is not enabled\. The rule is NON\_COMPLIANT if loggingLevel is neither ERROR nor INFO\.

**Identifier:** API\_GW\_EXECUTION\_LOGGING\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 loggingLevel  
\(Optional\) Comma\-separated list of specific logging levels \(for example, ERROR, INFO or ERROR,INFO\)\.

## AWS CloudFormation template<a name="w22aac11c29c17c29c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.