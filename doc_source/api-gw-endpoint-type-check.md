# api\-gw\-endpoint\-type\-check<a name="api-gw-endpoint-type-check"></a>

Checks that Amazon API Gateway APIs are of type as specified in the rule parameter '`endpointConfigurationTypes`'\. The rule returns COMPLIANT if any of the RestApi endpoint types matches the `endpointConfigurationTypes` configured in the rule parameter\. 

**Identifier:** API\_GW\_ENDPOINT\_TYPE\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

endpointConfigurationTypesType: String  
Comma\-separated list of allowed endpointConfigurationTypes\. Allowed values are REGIONAL, PRIVATE and EDGE\.

## AWS CloudFormation template<a name="w24aac11c29c17b7c15c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.