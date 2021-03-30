# redshift\-cluster\-configuration\-check<a name="redshift-cluster-configuration-check"></a>

Checks whether Amazon Redshift clusters have the specified settings\. 

**Identifier:** REDSHIFT\_CLUSTER\_CONFIGURATION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(Bahrain\) Region

**Parameters:**

clusterDbEncryptedType: booleanDefault: true  
Database encryption is enabled\.

loggingEnabledType: booleanDefault: true  
Audit logging is enabled\.

nodeTypes \(Optional\)Type: CSVDefault: dc1\.large  
Specify node type\.

## AWS CloudFormation template<a name="w26aac11c31c17b7d273c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.