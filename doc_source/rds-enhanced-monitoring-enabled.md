# rds\-enhanced\-monitoring\-enabled<a name="rds-enhanced-monitoring-enabled"></a>

Checks whether enhanced monitoring is enabled for Amazon Relational Database Service \(Amazon RDS\) instances\. 

**Identifier:** RDS\_ENHANCED\_MONITORING\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Osaka\) Region

**Parameters:**

monitoringInterval \(Optional\)Type: int  
An integer value in seconds between points when enhanced monitoring metrics are collected for the database instance\. The valid values are 1, 5, 10, 15, 30, and 60\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d287c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.