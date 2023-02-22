# opensearch\-encrypted\-at\-rest<a name="opensearch-encrypted-at-rest"></a>

Checks if Amazon OpenSearch Service domains have encryption at rest configuration enabled\. The rule is NON\_COMPLIANT if the `EncryptionAtRestOptions` field is not enabled\. 

**Note**  
The rule does not evaluate Elasticsearch domains\.

**Identifier:** OPENSEARCH\_ENCRYPTED\_AT\_REST

**Resource Types:** AWS::OpenSearch::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d407c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.