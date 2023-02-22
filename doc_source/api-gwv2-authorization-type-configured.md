# api\-gwv2\-authorization\-type\-configured<a name="api-gwv2-authorization-type-configured"></a>

Checks if Amazon API Gatewayv2 API routes have an authorization type set\. This rule is NON\_COMPLIANT if the authorization type is NONE\. 

**Identifier:** API\_GWV2\_AUTHORIZATION\_TYPE\_CONFIGURED

**Resource Types:** AWS::ApiGatewayV2::Route

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

authorizationType \(Optional\)Type: String  
Parameter to check API routes' authorization types against\. String parameters matching CUSTOM, AWS\_IAM, JWT are valid\.

## AWS CloudFormation template<a name="w2aac12c33c15b9c17c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.