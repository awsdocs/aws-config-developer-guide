# elasticsearch\-in\-vpc\-only<a name="elasticsearch-in-vpc-only"></a>

 Checks if Elasticsearch domains are in Amazon Virtual Private Cloud \(Amazon VPC\)\. The rule is NON\_COMPLIANT if an Elasticsearch domain endpoint is public\.

**Note**  
The rule does not evaluate Amazon OpenSearch Service domains\.

**Identifier:** ELASTICSEARCH\_IN\_VPC\_ONLY

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c31c27b9d275c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.