# opensearch\-https\-required<a name="opensearch-https-required"></a>

Checks whether connections to OpenSearch domains are using HTTPS\. The rule is NON\_COMPLIANT if the Amazon OpenSearch domain 'EnforceHTTPS' is not 'true' or is 'true' and 'TLSSecurityPolicy' is not in '`tlsPolicies`'\. 

**Identifier:** OPENSEARCH\_HTTPS\_REQUIRED

**Resource Types:** AWS::OpenSearch::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

tlsPolicies \(Optional\)Type: CSV  
Comma\-separated list of TLS security policies to check against the Amazon OpensSearch domain\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d439c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.