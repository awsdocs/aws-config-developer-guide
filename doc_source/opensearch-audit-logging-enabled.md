# opensearch\-audit\-logging\-enabled<a name="opensearch-audit-logging-enabled"></a>

Checks if Amazon OpenSearch Service domains have audit logging enabled\. The rule is NON\_COMPLIANT if an OpenSearch Service domain does not have audit logging enabled\. 

**Identifier:** OPENSEARCH\_AUDIT\_LOGGING\_ENABLED

**Resource Types:** AWS::OpenSearch::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

cloudWatchLogsLogGroupArnList \(Optional\)Type: CSV  
Comma\-separated list of Amazon CloudWatch Logs log groups that should be configured for audit logs\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d433c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.