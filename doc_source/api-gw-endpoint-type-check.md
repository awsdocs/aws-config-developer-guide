# api\-gw\-endpoint\-type\-check<a name="api-gw-endpoint-type-check"></a>

Checks that Amazon API Gateway APIs are of the type specified in the rule parameter `endpointConfigurationType`\. The rule returns NON\_COMPLIANT if the REST API does not match the endpoint type configured in the rule parameter\.

**Identifier:** API\_GW\_ENDPOINT\_TYPE\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 endpointConfigurationType  
\(Required\) Comma\-separated list of allowed endpoint types\. Allowed values are REGIONAL, PRIVATE and EDGE\.

## AWS CloudFormation template<a name="w22aac11c29c17c27c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.