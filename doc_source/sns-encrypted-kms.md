# sns\-encrypted\-kms<a name="sns-encrypted-kms"></a>

Checks if Amazon SNS topic is encrypted with AWS Key Management Service \(AWS KMS\)\. The rule is NON\_COMPLIANT if the Amazon SNS topic is not encrypted with AWS KMS\. The rule is also NON\_COMPLIANT when encrypted KMS key is not present in `kmsKeyIds` input parameter\.

**Identifier:** SNS\_ENCRYPTED\_KMS

**Resource Types:** AWS::SNS::Topic

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

kmsKeyIds \(Optional\)Type: CSV  
Comma separated list of AWS KMS key ARNs allowed for encrypting Amazon SNS Topic\.

## Proactive Evaluation<a name="w2aac12c33c15b9d587c17"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive)\. For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "KmsMasterKeyId": "my-kms-key-Id"
} 
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html)\. 

## AWS CloudFormation template<a name="w2aac12c33c15b9d587c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.