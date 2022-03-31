# opensearch\-data\-node\-fault\-tolerance<a name="opensearch-data-node-fault-tolerance"></a>

Checks if Amazon OpenSearch Service domains are configured with at least three data nodes and zoneAwarenessEnabled is true\. The rule is NON\_COMPLIANT for an OpenSearch domain if 'instanceCount' is less than 3 or 'zoneAwarenessEnabled' is set to 'false'\. 

**Identifier:** OPENSEARCH\_DATA\_NODE\_FAULT\_TOLERANCE

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w76aac11c31c17b7d353c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.