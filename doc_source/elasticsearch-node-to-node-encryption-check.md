# elasticsearch\-node\-to\-node\-encryption\-check<a name="elasticsearch-node-to-node-encryption-check"></a>

Check if Elasticsearch nodes are encrypted end to end\. The rule is NON\_COMPLIANT if the node\-to\-node encryption is not enabled on the domain\. 

**Note**  
The rule does not evaluate Amazon OpenSearch Service domains\.

**Identifier:** ELASTICSEARCH\_NODE\_TO\_NODE\_ENCRYPTION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Asia Pacific \(Osaka\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c31c27b9d279c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.