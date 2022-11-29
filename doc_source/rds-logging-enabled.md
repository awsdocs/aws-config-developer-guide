# rds\-logging\-enabled<a name="rds-logging-enabled"></a>

Checks that respective logs of Amazon Relational Database Service \(Amazon RDS\) are enabled\. The rule is NON\_COMPLIANT if any log types are not enabled\. 

**Identifier:** RDS\_LOGGING\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Asia Pacific \(Osaka\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

additionalLogs \(Optional\)Type: StringMap  
Comma\-separated list of engine names and log type names\. For example, "additionalLogs": "oracle: general, slowquery ; aurora: alert, slowquery"

## AWS CloudFormation template<a name="w2aac12c31c27b9d433c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.