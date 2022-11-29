# opensearch\-data\-node\-fault\-tolerance<a name="opensearch-data-node-fault-tolerance"></a>

Checks if Amazon OpenSearch Service domains are configured with at least three data nodes and zoneAwarenessEnabled is true\. The rule is NON\_COMPLIANT for an OpenSearch domain if 'instanceCount' is less than 3 or 'zoneAwarenessEnabled' is set to 'false'\. 

**Identifier:** OPENSEARCH\_DATA\_NODE\_FAULT\_TOLERANCE

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Osaka\), Europe \(Milan\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c31c27b9d395c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.