# elasticsearch\-encrypted\-at\-rest<a name="elasticsearch-encrypted-at-rest"></a>

Checks if Elasticsearch domains have encryption at rest configuration enabled\. The rule is NON\_COMPLIANT if the `EncryptionAtRestOptions` field is not enabled\.

**Note**  
The rule does not evaluate Amazon OpenSearch Service domains\.

**Identifier:** ELASTICSEARCH\_ENCRYPTED\_AT\_REST

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d281c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.