# opensearch\-node\-to\-node\-encryption\-check<a name="opensearch-node-to-node-encryption-check"></a>

Check if Amazon OpenSearch Service nodes are encrypted end to end\. The rule is NON\_COMPLIANT if the node\-to\-node encryption is not enabled on the domain 

**Note**  
The rule does not evaluate Elasticsearch domains\.

**Identifier:** OPENSEARCH\_NODE\_TO\_NODE\_ENCRYPTION\_CHECK

**Resource Types:** AWS::OpenSearch::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d445c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.