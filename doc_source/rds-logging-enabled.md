# rds\-logging\-enabled<a name="rds-logging-enabled"></a>

Checks that respective logs of Amazon Relational Database Service \(Amazon RDS\) are enabled\. The rule is NON\_COMPLIANT if any log types are not enabled\. 

**Note**  
DB Instances that are not in 'available', 'backing\-up', 'storage\-optimization', or 'storage\-full' status evaluate as `NOT_APPLICABLE`\.

**Identifier:** RDS\_LOGGING\_ENABLED

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Africa \(Cape Town\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

additionalLogs \(Optional\)Type: StringMap  
Comma\-separated list of engine names and log type names\. For example, "additionalLogs": "oracle: general, slowquery ; aurora: alert, slowquery"

## AWS CloudFormation template<a name="w2aac12c33c15b9d473c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.