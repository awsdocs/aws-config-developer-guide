# rds\-cluster\-default\-admin\-check<a name="rds-cluster-default-admin-check"></a>

Checks if an Amazon Relational Database Service \(Amazon RDS\) database cluster has changed the admin username from its default value\. The rule is NON\_COMPLIANT if the admin username is set to the default value\. 

**Identifier:** RDS\_CLUSTER\_DEFAULT\_ADMIN\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Middle East \(Bahrain\), South America \(Sao Paulo\) Region

**Parameters:**

validAdminUserNames \(Optional\)Type: CSV  
Comma\-separated list of admin username\(s\) that Amazon RDS clusters can use\. Cannot include 'postgres' or 'admin' as valid username\(s\) as these are default values\.

## AWS CloudFormation template<a name="w79aac11c32c17b9d409c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.