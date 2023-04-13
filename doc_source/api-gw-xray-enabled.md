# api\-gw\-xray\-enabled<a name="api-gw-xray-enabled"></a>

Checks if AWS X\-Ray tracing is enabled on Amazon API Gateway REST APIs\. The rule is COMPLIANT if X\-Ray tracing is enabled and NON\_COMPLIANT otherwise\. 

**Identifier:** API\_GW\_XRAY\_ENABLED

**Resource Types:** AWS::ApiGateway::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## Proactive Evaluation<a name="w2aac12c33c15b9c31c17"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive)\. For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "TracingEnabled": BOOLEAN,
   "RestApiId": "my-rest-api-Id",
} 
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html)\. 

## AWS CloudFormation template<a name="w2aac12c33c15b9c31c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.