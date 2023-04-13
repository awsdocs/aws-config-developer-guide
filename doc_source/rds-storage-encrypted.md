# rds\-storage\-encrypted<a name="rds-storage-encrypted"></a>

Checks if storage encryption is enabled for your RDS DB instances\. The rule is NON\_COMPLIANT if storage encryption is not enabled\.

**Identifier:** RDS\_STORAGE\_ENCRYPTED

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

kmsKeyId \(Optional\)Type: String  
KMS key ID or Amazon Resource Name \(ARN\) used to encrypt the storage\.

## Proactive Evaluation<a name="w2aac12c33c15b9d483c17"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive)\. For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "StorageEncrypted": BOOLEAN
} 
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html)\. 

## AWS CloudFormation template<a name="w2aac12c33c15b9d483c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.