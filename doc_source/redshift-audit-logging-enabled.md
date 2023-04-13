# redshift\-audit\-logging\-enabled<a name="redshift-audit-logging-enabled"></a>

Checks if Amazon Redshift clusters are logging audits to a specific bucket\. The rule is NON\_COMPLIANT if audit logging is not enabled for a Redshift cluster or if the '`bucketNames`' parameter is provided but the audit logging destination does not match\. 

**Identifier:** REDSHIFT\_AUDIT\_LOGGING\_ENABLED

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

bucketNames \(Optional\)Type: CSV  
Comma\-separated list of Amazon S3 bucket names for storing audit logs\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d485c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.