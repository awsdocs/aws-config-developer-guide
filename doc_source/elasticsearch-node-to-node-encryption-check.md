# elasticsearch\-node\-to\-node\-encryption\-check<a name="elasticsearch-node-to-node-encryption-check"></a>

Check if Elasticsearch nodes are encrypted end to end\. The rule is NON\_COMPLIANT if the node\-to\-node encryption is not enabled on the domain\. 

**Note**  
The rule does not evaluate Amazon OpenSearch Service domains\.

**Identifier:** ELASTICSEARCH\_NODE\_TO\_NODE\_ENCRYPTION\_CHECK

**Resource Types:** AWS::Elasticsearch::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## Proactive Evaluation<a name="w2aac12c33c15b9d313c19"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive)\. For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "NodeToNodeEncryptionOptions": BOOLEAN
} 
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html)\. 

## AWS CloudFormation template<a name="w2aac12c33c15b9d313c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.