# opensearch\-https\-required<a name="opensearch-https-required"></a>

Checks whether connections to OpenSearch domains are using HTTPS\. The rule is NON\_COMPLIANT if the Amazon OpenSearch domain 'EnforceHTTPS' is not 'true' or is 'true' and 'TLSSecurityPolicy' is not in '`tlsPolicies`'\. 

**Identifier:** OPENSEARCH\_HTTPS\_REQUIRED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

tlsPolicies \(Optional\)Type: CSV  
Comma\-separated list of TLS security policies to check against the Amazon OpensSearch domain\.

## AWS CloudFormation template<a name="w76aac11c31c17b7d357c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.