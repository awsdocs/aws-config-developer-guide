# opensearch\-in\-vpc\-only<a name="opensearch-in-vpc-only"></a>

Checks if Amazon OpenSearch Service domains are in an Amazon Virtual Private Cloud \(VPC\)\. The rule is NON\_COMPLIANT if an OpenSearch Service domain endpoint is public\. 

**Note**  
The rule does not evaluate Elasticsearch domains\.

**Identifier:** OPENSEARCH\_IN\_VPC\_ONLY

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Osaka\), Europe \(Milan\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c31c27b9d401c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.