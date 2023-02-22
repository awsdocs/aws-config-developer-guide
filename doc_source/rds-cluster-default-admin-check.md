# rds\-cluster\-default\-admin\-check<a name="rds-cluster-default-admin-check"></a>

Checks if an Amazon Relational Database Service \(Amazon RDS\) database cluster has changed the admin username from its default value\. The rule is NON\_COMPLIANT if the admin username is set to the default value\. 

**Identifier:** RDS\_CLUSTER\_DEFAULT\_ADMIN\_CHECK

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(Bahrain\), China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), South America \(Sao Paulo\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

validAdminUserNames \(Optional\)Type: CSV  
Comma\-separated list of admin username\(s\) that Amazon RDS clusters can use\. Cannot include 'postgres' or 'admin' as valid username\(s\) as these are default values\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d419c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.