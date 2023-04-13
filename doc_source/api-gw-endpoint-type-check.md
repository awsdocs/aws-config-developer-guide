# api\-gw\-endpoint\-type\-check<a name="api-gw-endpoint-type-check"></a>

Checks if Amazon API Gateway APIs are of the type specified in the rule parameter `endpointConfigurationType`\. The rule returns NON\_COMPLIANT if the REST API does not match the endpoint type configured in the rule parameter\.

**Identifier:** API\_GW\_ENDPOINT\_TYPE\_CHECK

**Resource Types:** AWS::ApiGateway::RestApi

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

endpointConfigurationTypesType: String  
Comma\-separated list of allowed endpointConfigurationTypes\. Allowed values are REGIONAL, PRIVATE and EDGE\.

## AWS CloudFormation template<a name="w2aac12c33c15b9c25c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.