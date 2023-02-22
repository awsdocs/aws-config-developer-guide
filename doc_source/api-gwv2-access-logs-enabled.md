# api\-gwv2\-access\-logs\-enabled<a name="api-gwv2-access-logs-enabled"></a>

Checks if Amazon API Gateway V2 stages have access logging enabled\. The rule is NON\_COMPLIANT if 'accessLogSettings' is not present in Stage configuration\. 

**Identifier:** API\_GWV2\_ACCESS\_LOGS\_ENABLED

**Resource Types:** AWS::ApiGatewayV2::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9c15c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.