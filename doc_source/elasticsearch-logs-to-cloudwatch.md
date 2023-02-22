# elasticsearch\-logs\-to\-cloudwatch<a name="elasticsearch-logs-to-cloudwatch"></a>

Checks if Elasticsearch domains are configured to send logs to Amazon CloudWatch Logs\. The rule is COMPLIANT if a log is enabled for an Elasticsearch domain\. This rule is NON\_COMPLIANT if logging is not configured\. 

**Note**  
The rule does not evaluate Amazon OpenSearch Service domains\.

**Identifier:** ELASTICSEARCH\_LOGS\_TO\_CLOUDWATCH

**Resource Types:** AWS::Elasticsearch::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

logTypes \(Optional\)Type: CSV  
Comma\-separated list of logs that are enabled\. Valid values are 'search', 'index', 'error'\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d285c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.