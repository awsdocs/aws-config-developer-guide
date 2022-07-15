# redshift\-audit\-logging\-enabled<a name="redshift-audit-logging-enabled"></a>

Checks if Amazon Redshift clusters are logging audits to a specific bucket\. The rule is NON\_COMPLIANT if audit logging is not enabled for a Redshift cluster or if the '`bucketNames`' parameter is provided but the audit logging destination does not match\. 

**Identifier:** REDSHIFT\_AUDIT\_LOGGING\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\) Region

**Parameters:**

bucketNames \(Optional\)Type: CSV  
Comma\-separated list of Amazon S3 bucket names for storing audit logs\.

## AWS CloudFormation template<a name="w79aac11c32c17b9d445c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.