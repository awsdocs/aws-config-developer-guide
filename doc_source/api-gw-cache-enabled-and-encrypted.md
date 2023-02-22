# api\-gw\-cache\-enabled\-and\-encrypted<a name="api-gw-cache-enabled-and-encrypted"></a>

Checks that all methods in Amazon API Gateway stages have cache enabled and cache encrypted\. The rule is NON\_COMPLIANT if any method in Amazon API Gateway stage is not configured to cache or the cache is not encrypted\. 

**Identifier:** API\_GW\_CACHE\_ENABLED\_AND\_ENCRYPTED

**Resource Types:** AWS::ApiGateway::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9c21c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.