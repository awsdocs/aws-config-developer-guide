# appsync\-logging\-enabled<a name="appsync-logging-enabled"></a>

Checks if an AWS AppSync API has logging enabled\. The rule is NON\_COMPLIANT if logging is not enabled, or 'fieldLogLevel' is neither ERROR nor ALL\. 

**Identifier:** APPSYNC\_LOGGING\_ENABLED

**Resource Types:** AWS::AppSync::GraphQLApi

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

fieldLoggingLevel \(Optional\)Type: CSV  
Comma\-separated list of specific field logging levels \(for example, ERROR, ALL\)\.

## AWS CloudFormation template<a name="w2aac12c33c15b9c41c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.