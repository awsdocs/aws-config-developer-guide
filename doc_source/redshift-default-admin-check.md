# redshift\-default\-admin\-check<a name="redshift-default-admin-check"></a>

Checks if an Amazon Redshift cluster has changed the admin username from its default value\. The rule is NON\_COMPLIANT if the admin username for a Redshift cluster is set to “awsuser” or if the username does not match what is listed in parameter\. 

**Identifier:** REDSHIFT\_DEFAULT\_ADMIN\_CHECK

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), China \(Ningxia\) Region

**Parameters:**

validAdminUserNames \(Optional\)Type: CSV  
Comma\-separated list of admin username\(s\) for Redshift clusters to use\. Note: 'awsuser' is the default and not accepted\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d497c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.