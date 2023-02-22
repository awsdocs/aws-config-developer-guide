# opensearch\-logs\-to\-cloudwatch<a name="opensearch-logs-to-cloudwatch"></a>

Checks if Amazon OpenSearch Service domains are configured to send logs to Amazon CloudWatch Logs\. The rule is NON\_COMPLIANT if logging is not configured\. 

**Note**  
The rule does not evaluate Elasticsearch domains\.

**Identifier:** OPENSEARCH\_LOGS\_TO\_CLOUDWATCH

**Resource Types:** AWS::OpenSearch::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

logTypes \(Optional\)Type: CSV  
Comma\-separated list of logs that are enabled\. Valid values are 'search', 'index', 'error'\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d413c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.