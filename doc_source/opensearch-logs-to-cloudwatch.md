# opensearch\-logs\-to\-cloudwatch<a name="opensearch-logs-to-cloudwatch"></a>

Checks if Amazon OpenSearch Service domains are configured to send logs to Amazon CloudWatch Logs\. The rule is NON\_COMPLIANT if logging is not configured\. 

**Identifier:** OPENSEARCH\_LOGS\_TO\_CLOUDWATCH

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

logTypes \(Optional\)Type: CSV  
Comma\-separated list of logs that are enabled\. Valid values are 'search', 'index', 'error'\.

## AWS CloudFormation template<a name="w85aac12c32c17b9d403c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.