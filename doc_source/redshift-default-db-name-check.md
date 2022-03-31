# redshift\-default\-db\-name\-check<a name="redshift-default-db-name-check"></a>

Checks if a Redshift cluster has changed its database name from the default value\. The rule is NON\_COMPLIANT if the database name for a Redshift cluster is set to “dev”, or if the optional parameter is provided and the database name does not match\. 

**Identifier:** REDSHIFT\_DEFAULT\_DB\_NAME\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

validDatabaseNames \(Optional\)Type: CSV  
Comma\-separated list of database name\(s\) for Redshift clusters\.

## AWS CloudFormation template<a name="w76aac11c31c17b7d413c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.